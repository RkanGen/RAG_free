
# RAG_free

Free RAG  is a Retrieval-Augmented Generation (RAG) system designed to process and query PDF and CSV documents using free APIs "(free tiers)" like Groq , Pinecone, and Gemini. The system provides a web-based interface where users can upload documents, initialize the system with their API keys, and interact with the documents through natural language queries.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Initializing the System](#initializing-the-system)
  - [Uploading and Ingesting Documents](#uploading-and-ingesting-documents)
  - [Querying the Documents](#querying-the-documents)
  - [Copying Responses](#copying-responses)
- [Environment Variables](#environment-variables)
- [APIs Used](#apis-used)
- [Contributing](#contributing)


## Introduction

Free RAG_PDF leverages state-of-the-art language models and vector stores to make it easy to query and retrieve relevant information from your documents. The interface is built using Gradio, providing a user-friendly way to interact with the system without needing to dive into the code.

## Features

- **API Integration**: Easily integrate with Groq, Pinecone, and Gemini APIs for document processing and query handling.
- **Document Ingestion**: Upload and ingest PDF or CSV documents for processing.
- **Query System**: Query the ingested documents and retrieve relevant content.
- **Copy Response**: Quickly copy the query response to your clipboard for easy sharing.

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
   python app.py
   ```

## Usage

### Initializing the System

1. Open the Gradio interface in your browser.
2. Enter your API keys for Llama Cloud, Groq, Google, and Pinecone.
3. Click the **Initialize System** button to set up the system with your API keys.

### Uploading and Ingesting Documents

1. Use the **Upload PDF/CSV Document** button to select a file from your computer.
2. Click **Ingest Document** to process and store the document's content in the vector store.

### Querying the Documents

1. Enter your query in the **Query** textbox.
2. Click **Submit Query** to retrieve relevant information from the ingested documents.
3. View the response in the **Query Output** textbox.

### Copying Responses

1. After receiving a query response, click the **Copy Response** button.
2. The response will be copied to your clipboard, and you'll receive a confirmation message.

## Environment Variables

You'll need to set the following environment variables in a `.env` file:

- `LLAMA_CLOUD_API_KEY`: Your API key for LlamaParse.
- `GROQ_API_KEY`: Your API key for Groq.
- `GOOGLE_API_KEY`: Your API key for GeminiEmbedding.
- `PINECONE_API_KEY`: Your API key for Pinecone.

### Example `.env` file:
```env
LLAMA_CLOUD_API_KEY=your-llama-cloud-api-key
GROQ_API_KEY=your-groq-api-key
GOOGLE_API_KEY=your-google-api-key
PINECONE_API_KEY=your-pinecone-api-key
```

## APIs Used

- **LlamaParse**: For parsing PDF documents into Markdown format.
- **Groq**: Language model used for text processing and understanding.
- **GeminiEmbedding**: Generates embeddings for text chunks.
- **Pinecone**: Vector store for storing and retrieving document embeddings.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Feel free to open issues for any bugs or feature requests.



---

