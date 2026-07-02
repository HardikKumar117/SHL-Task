from langchain.tools import tool
import chromadb
from sentence_transformers import SentenceTransformer





@tool
def search_tool(query: str) -> str:
    """Searches for relevant information based on the query. in the shl catalog """
    # Implement your search logic here
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode([query])  
    embedded_query = embeddings[0]
    chroma_client = chromadb.PersistentClient(path="./vector_store")
    
    collection=chroma_client.get_collection(name="vector_store")
    results = collection.query(
        query_embeddings=[embedded_query],
        n_results=10
    )
    docs = results["documents"][0]
    print(results)

    return [
        {
            "name": metadata["name"],
            "url": metadata["url"],
            "test_type": metadata["test_type"]
        }
        for metadata in results["metadatas"][0]
    ]

