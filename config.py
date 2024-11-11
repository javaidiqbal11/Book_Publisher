from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Configuration settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))  # Default to 6333 if not set
CHUNK_SIZE = 50000000
QDRANT_COLLECTION_NAME = "book_collection"  # Define your collection name here
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 6000))  