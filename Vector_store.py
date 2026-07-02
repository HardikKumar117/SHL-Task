from sentence_transformers import SentenceTransformer
from typing import List
from langchain_core.documents import Document
import chromadb

def build_vector_store(docs: List[Document]):
    """
    Build a vector store using the SentenceTransformer model.
    """
    # Load the pre-trained SentenceTransformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # You can add code here to create and populate your vector store using the model
    # For example, you might want to encode some text data and store the embeddings
    embeddings = model.encode([doc.page_content for doc in docs])
    chroma_client = chromadb.PersistentClient(path="./vector_store")
    collection = chroma_client.get_or_create_collection(name="vector_store")

    document_ids = [f"doc_{index}" for index in range(len(docs))]
    collection.add(
        ids=document_ids,
        documents=[doc.page_content for doc in docs],
        metadatas=[doc.metadata for doc in docs],
        embeddings=embeddings,
    )
    return collection