import gradio as gr
import os
import nest_asyncio
from dotenv import load_dotenv
from langchain.llms import Groq
from langchain.embeddings import GeminiEmbedding
from llama_index.core import Settings, SimpleDirectoryReader
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from pinecone import Pinecone
from llama_parse import LlamaParse

nest_asyncio.apply()

# Function to set API keys and initialize components
def initialize_system(llama_cloud_api_key, groq_api_key, google_api_key, pinecone_api_key):
    # Save API keys to environment variables
    os.environ['LLAMA_CLOUD_API_KEY'] = llama_cloud_api_key
    os.environ['GROQ_API_KEY'] = groq_api_key
    os.environ['GOOGLE_API_KEY'] = google_api_key
    os.environ['PINECONE_API_KEY'] = pinecone_api_key
    
    # Initialize components with the provided API keys
    llm = Groq(model="llama-3.1-70b-versatile", api_key=groq_api_key)
    embedding_model = GeminiEmbedding(model="models/embedding-001", api_key=google_api_key)
    
    Settings.llm = llm
    Settings.embed_model = embedding_model
    Settings.chunk_size = 1024
    
    pinecone_client = Pinecone(api_key=pinecone_api_key)
    pinecone_index = pinecone_client.Index('project-1')
    vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
    
    return "System initialized successfully!"

# Function to ingest the uploaded document
def ingest_document(file):
    parser = LlamaParse(api_key=os.getenv("LLAMA_CLOUD_API_KEY"), result_type="markdown", verbose=True)
    file_extractor = {".pdf": parser}
    
    # Assuming the document is uploaded to a temporary file
    documents = SimpleDirectoryReader(file.name, file_extractor=file_extractor).load_data()
    
    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=1024, chunk_overlap=25),
            embedding_model
        ],
        vector_store=vector_store
    )
    pipeline.run(documents=documents)
    
    return "Document ingested successfully!"

# Function to query the document
def query_document(query):
    response = query_engine.query(query)
    return response

# Gradio interface
with gr.Blocks() as interface:
    gr.Markdown("# Free RAG_PDF Interface")
    
    with gr.Row():
        llama_cloud_api_key = gr.Textbox(label="Llama Cloud API Key", type="password")
        groq_api_key = gr.Textbox(label="Groq API Key", type="password")
        google_api_key = gr.Textbox(label="Google API Key", type="password")
        pinecone_api_key = gr.Textbox(label="Pinecone API Key", type="password")
    
    initialize_button = gr.Button("Initialize System")
    
    initialize_output = gr.Textbox(label="Initialization Output", interactive=False)
    
    with gr.Row():
        file_upload = gr.File(label="Upload PDF/CSV Document", file_types=["pdf", "csv"])
        ingest_button = gr.Button("Ingest Document")
    
    ingest_output = gr.Textbox(label="Ingestion Output", interactive=False)
    
    with gr.Row():
        query_input = gr.Textbox(label="Query", placeholder="Ask a question about the document...")
        query_button = gr.Button("Submit Query")
    
    query_output = gr.Textbox(label="Query Output", interactive=False)
    copy_button = gr.Button("Copy Response")
    
    # Link the initialize button to the initialization function
    initialize_button.click(fn=initialize_system, 
                            inputs=[llama_cloud_api_key, groq_api_key, google_api_key, pinecone_api_key], 
                            outputs=initialize_output)
    
    # Link the ingest button to the document ingestion function
    ingest_button.click(fn=ingest_document, inputs=file_upload, outputs=ingest_output)
    
    # Link the query button to the query function
    query_button.click(fn=query_document, inputs=query_input, outputs=query_output)
    
    # Copy button functionality
    def copy_to_clipboard(text):
        import pyperclip
        pyperclip.copy(text)
        return "Copied to clipboard!"
    
    copy_button.click(fn=copy_to_clipboard, inputs=query_output, outputs=gr.Textbox(label="Copy Status", interactive=False))

# Launch the Gradio interface
interface.launch()
