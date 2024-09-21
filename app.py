import streamlit as st
from backend import process_pdf, query_rag

st.set_page_config(page_title="PDF QA Bot", layout="wide")

# Custom CSS to enhance the interface
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
    }
    .st-emotion-cache-1v0mbdj {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("📚 PDF Question Answering Bot")

# Initialize session state
if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = None
if 'file_processed' not in st.session_state:
    st.session_state.file_processed = False

# Create two columns
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.header("📄 Upload PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        if st.button("Process PDF"):
            with st.spinner("Processing PDF..."):
                st.session_state.vectorstore = process_pdf(uploaded_file)
                st.session_state.file_processed = True
            st.success("PDF processed successfully!")

with col2:
    st.header("❓ Ask a Question")
    user_question = st.text_input("Enter your question about the PDF content:")
    
    if user_question and st.session_state.file_processed:
        if st.button("Get Answer"):
            with st.spinner("Generating answer..."):
                answer = query_rag(user_question, st.session_state.vectorstore)
            st.subheader("Answer:")
            st.write(answer)
    elif not st.session_state.file_processed:
        st.info("Please upload and process a PDF before asking questions.")

# Add a footer
st.markdown("---")
st.markdown("Made with ❤️ by Rkan")
