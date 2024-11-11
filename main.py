import gradio as gr
from utils.html_reader import read_book_content
from utils.text_processing import chunk_text, generate_embedding, summarize_text, rephrase_text
from utils.embedding_storage import initialize_qdrant_collection, store_embeddings
from config import QDRANT_HOST, QDRANT_PORT

# Initialize Qdrant collection dynamically
def initialize_qdrant_collection_if_needed(embedding_size):
    initialize_qdrant_collection(vector_size=embedding_size)

# Gradio processing function
def process_book(html_file, image_folder):
    # Load relevant book content and images based on keywords
    book_content, images = read_book_content(html_file, image_folder)
    
    rephrased_chapter = rephrase_text(book_content)

    introduction_summary = summarize_text(book_content)
    

    return introduction_summary,rephrased_chapter

# Gradio interface setup
iface = gr.Interface(
    fn=process_book,
    inputs=[
        gr.File(label="Upload HTML File"),
        gr.Textbox(label="Image Folder Path")
    ],
    outputs=[
        gr.Textbox(label="Summary of Introduction"),
        gr.Textbox(label="5000-Words Rephrased Introduction")
    ],
    title="Book Publisher",
    description="Upload an HTML file and related images to generate a summary, rephrase content, and store data in Qdrant."
)

# Start the app
if __name__ == "__main__":
    iface.launch(share=True)
