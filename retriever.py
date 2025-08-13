# retriever.py

from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
import os

def setup_vectorstore():
    # Load the sentence transformer model
    model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Read knowledge base from a local text file
    with open('data/insurance_docs.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split the content into chunks (based on empty lines)
    chunks = content.split('\n\n')
    
    # Wrap each chunk as a Document object
    documents = [Document(page_content=chunk) for chunk in chunks if chunk.strip()]
    
    # Build the vectorstore (FAISS index)
    vectorstore = FAISS.from_documents(documents, embedding=model)
    
    # Return a retriever interface
    return vectorstore.as_retriever()
