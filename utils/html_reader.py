import re
from bs4 import BeautifulSoup
import os

def read_book_content(html_file, image_folder):
    # Read HTML file content
    with open(html_file, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        text = soup.get_text()

    # Optionally, load images from the image folder if needed
    images = []
    if os.path.isdir(image_folder):
        images = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, img))]

    return text, images
