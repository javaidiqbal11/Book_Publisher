import uuid
from qdrant_client import QdrantClient
from qdrant_client.http import models as qdrant_models
from config import QDRANT_HOST, QDRANT_PORT, QDRANT_COLLECTION_NAME

client = QdrantClient(QDRANT_HOST, port=QDRANT_PORT)

def initialize_qdrant_collection(vector_size):
    client.recreate_collection(
        collection_name=QDRANT_COLLECTION_NAME,
        vectors_config=qdrant_models.VectorParams(size=vector_size, distance="Cosine")
    )


def store_embeddings(text, embedding, label):
    # Generate a valid UUID and convert it to a string
    point_id = str(uuid.uuid4())
    point = qdrant_models.PointStruct(
        id=point_id,  # Use string representation of UUID
        vector=embedding,
        payload={"text": text, "label": label}
    )
    client.upsert(collection_name=QDRANT_COLLECTION_NAME, points=[point])



def query_embeddings(query_text, embedding_func):
    query_embedding = embedding_func(query_text)
    search_result = client.search(
        collection_name=QDRANT_COLLECTION_NAME,
        query_vector=query_embedding,
        limit=5
    )
    return [point.payload["text"] for point in search_result]
