
# RAG_free

This project is a Retrieval-Augmented Generation (RAG) system, designed to process documents (PDF format), store document embeddings in a Pinecone vector store, and retrieve contextually relevant information using Groq's Llama-3 model for generating answers.
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Uploading and Ingesting Documents](#uploading-and-ingesting-documents)
  - [Querying the Documents](#querying-the-documents)
- [Environment Variables](#environment-variables)
- [APIs Used](#apis-used)
- [Contributing](#contributing)
![ragger](https://github.com/user-attachments/assets/9761074d-e449-4dbf-b9b3-96e29465926a)


## Introduction

Free RAG_PDF leverages state-of-the-art language models and vector stores to make it easy to query and retrieve relevant information from your documents. The interface is built using Streamlit, providing a user-friendly way to interact with the system without needing to dive into the code.

## Features

-PDF Document Processing: Load and split PDF files into chunks.
-Pinecone Vector Store: Store embeddings of the document texts using the sentence-transformers/all-MiniLM-L6-v2 model.
-Retrieval-Augmented Generation (RAG): Retrieve relevant document chunks based on a query and generate an answer using Groq's LLM.

## Installation

To get started with Free RAG PDF, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RkanGen/RAG_free.git
   cd RAG_free
   ```

2. **Install the Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Your Environment Variables**:
   See the [Environment Variables](#environment-variables) section for more details.

4. **Run the Application**:
   Launch the Gradio interface:
   ```bash
   streamlit run app.py
   ```

## Usage




### Uploading and Ingesting Documents

1. Use the **Upload PDF/CSV Document** button to select a file from your computer.
2. Click **Process PDF Document** to process and store the document's content in the vector store(pinecone).

### Querying the Documents

1. Enter your query in the **Query** textbox.
2. Click **Submit Query** to retrieve relevant information from the ingested documents.
3. View the response in the **Query Output** textbox.
![rag2](https://github.com/user-attachments/assets/bf0bb5ef-d8eb-4d70-9f51-1b3825ee3c8e)

### Copying Responses

1. After receiving a query response, click the **Copy Response** button.
2. The response will be copied to your clipboard, and you'll receive a confirmation message.

## Environment Variables

You'll need to set the following environment variables in a `.env` file:

- `GROQ_API_KEY`: Your API key for Groq.
- sentence-transformers/all-MiniLM-L6-v2 for embedding documents 
- `PINECONE_API_KEY`: Your API key for Pinecone.

### Example `.env` file:
```env

GROQ_API_KEY=your-groq-api-key
PINECONE_API_KEY=your-pinecone-api-key
```

## APIs Used

- **Groq**: Language model used for text processing and understanding.

- **Pinecone**: Vector store for storing and retrieving document embeddings.
U can use jina ai for embedding !!! and provide their API_KEY
## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Feel free to open issues for any bugs or feature requests.



---

