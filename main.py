# import gradio as gr
# from utils.html_reader import read_book_content
# from utils.text_processing import chunk_text, generate_embedding, summarize_text, rephrase_text
# from utils.embedding_storage import initialize_qdrant_collection, store_embeddings
# from config import QDRANT_HOST, QDRANT_PORT

# # Initialize Qdrant collection dynamically
# def initialize_qdrant_collection_if_needed(embedding_size):
#     initialize_qdrant_collection(vector_size=embedding_size)

# # Gradio processing function
# def process_book(html_file, image_folder):
#     # Load relevant book content and images based on keywords
#     book_content, images = read_book_content(html_file, image_folder)
    
#     rephrased_chapter = rephrase_text(book_content)

#     introduction_summary = summarize_text(book_content)
    

#     return introduction_summary,rephrased_chapter

# # Gradio interface setup
# iface = gr.Interface(
#     fn=process_book,
#     inputs=[
#         gr.File(label="Upload HTML File"),
#         gr.Textbox(label="Image Folder Path")
#     ],
#     outputs=[
#         gr.Textbox(label="Summary of Introduction"),
#         gr.Textbox(label="5000-Words Rephrased Introduction")
#     ],
#     title="Book Publisher",
#     description="Upload an HTML file and related images to generate a summary, rephrase content, and store data in Qdrant."
# )

# # Start the app
# if __name__ == "__main__":
#     iface.launch(share=True)


#######################

import gradio as gr
import os
from utils.html_reader import read_book_content
from utils.text_processing import chunk_text, generate_embedding, summarize_text, rephrase_text
from utils.embedding_storage import initialize_qdrant_collection, store_embeddings
from config import QDRANT_HOST, QDRANT_PORT

# Path to the folder containing all book folders
DATA_FOLDER = "data"

# Initialize Qdrant collection dynamically
def initialize_qdrant_collection_if_needed(embedding_size):
    initialize_qdrant_collection(vector_size=embedding_size)

# List available books in the data folder
def list_books():
    books = {}
    for folder in os.listdir(DATA_FOLDER):
        folder_path = os.path.join(DATA_FOLDER, folder)
        if os.path.isdir(folder_path):
            # Look for an HTML file inside each book folder
            for file in os.listdir(folder_path):
                if file.endswith(".html"):
                    books[folder] = (os.path.join(folder_path, file), folder_path)  # {folder name: (HTML path, image folder)}
                    break
    return books

# Gradio processing function
def process_book(selected_book):
    books = list_books()
    if selected_book not in books:
        return "Error: Book not found.", ""
    
    html_file, image_folder = books[selected_book]
    # Load relevant book content and images based on keywords
    book_content, images = read_book_content(html_file, image_folder)
    
    rephrased_chapter = rephrase_text(book_content)
    introduction_summary = summarize_text(book_content)
    
    return introduction_summary, rephrased_chapter

# Setup the dropdown options based on available books
book_options = list_books()
book_choices = list(book_options.keys())  # Only the folder names as dropdown values

# # Gradio interface setup
# iface = gr.Interface(
#     fn=process_book,
#     inputs=[
#         gr.Dropdown(label="Select Book", choices=book_choices),
#     ],
#     outputs=[
#         gr.Textbox(label="Summary of Introduction"),
#         gr.Textbox(label="5000-Words Rephrased Introduction")
#     ],
#     title="Book Publisher",
#     description="Select a book to generate a summary, rephrase content, and store data in Qdrant."
# )

# # Start the app
# if __name__ == "__main__":
#     iface.launch(share=True)

example_inputs = [[book] for book in book_choices]

# Gradio interface setup
iface = gr.Interface(
    fn=process_book,
    inputs=[
        gr.Dropdown(label="Select Book", choices=book_choices),
    ],
    outputs=[
        gr.Textbox(label="Summary of Introduction"),
        gr.Textbox(label="5000-Words Rephrased Introduction")
    ],
    examples=example_inputs,  # Add examples here
    title="Book Publisher",
    description="Select a book to generate a summary, rephrase content, and store data in Qdrant."
)

# Start the app
if __name__ == "__main__":
    iface.launch(share=True)
