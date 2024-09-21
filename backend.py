import os
import getpass
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
load_dotenv()

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Initialize embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize Groq model
if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")

llm = ChatGroq(
    model_name="llama3-8b-8192",
    temperature=1,
    max_tokens=1024,
    top_p=1
)

def process_pdf(file):
    # Create a temporary file
    with open("temp.pdf", "wb") as f:
        f.write(file.getvalue())
    
    # Load PDF
    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()
    
    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    
    # Create or load Pinecone index
    index_name = "rag-index"
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=384,  # 384 for all-MiniLM-L6-v2
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
    
    # Create vector store
    index = pc.Index(index_name)
    vectorstore = Pinecone(index, embeddings.embed_query, "text")
    
    # Upsert documents
    vectorstore.add_documents(texts)
    
    # Remove temporary file
    os.remove("temp.pdf")
    
    return vectorstore

def query_rag(query, vectorstore):
    # Create retrieval chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    
    # Get answer
    answer = qa_chain.run(query)
    
    return answer
