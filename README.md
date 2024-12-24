# Amazon Book Publisher 
The Book Publisher is a Python application that processes Amazon eBook content by extracting, summarizing, and rephrasing introduction section. This application leverages Gradio for an interactive interface, Qdrant for embedding storage, and OpenAI models for text processing.

---
## Features
- Automatic Book Content Selection: Selects eBook HTML content from available files in the data folder.
- Content Summarization: Summarizes the introductory content of eBooks.
- Content Rephrasing: Rephrases sections of eBook content.
- Embedding Storage: Stores content embeddings in Qdrant for future retrieval and analysis.
- Pattern Matching: Extracts specific sections using flexible pattern matching to recognize a variety of eBook heading styles.
- Book Description: Update book description based on the keywords/tags. 

## Installation
1- Clone the repository:
```shell
git clone https://github.com/yourusername/book-publisher.git
cd book-publisher
```
2- Create a virtual environment and activate it:
```shell
python3 -m venv env
source env/bin/activate
```
3- Install dependencies:
```shell
pip install -r requirements.txt
```
## Configuration
1- Qdrant Configuration:
Configure Qdrant connection details in config.py:
```shell
QDRANT_HOST = "localhost"  # or your Qdrant host
QDRANT_PORT = 6333         # or your Qdrant port
```

2- OpenAI API Key:
Set your OpenAI API key in an environment variable:
```shell
export OPENAI_API_KEY="your_openai_api_key"
```
## Usage
1- Add Book Data:

- Place book folders containing HTML files and images in the data directory. Ensure that each folder has a unique name, and the HTML file is named appropriately (e.g., pg74725-h.html).

2- Run the Application:
- Start the Gradio application with:
```shell
python main.py
```
3- Using the Interface:
- Select a book from the dropdown list populated by available book folders in data.
- The application will display a summary and a rephrased version of the introductory content.

## Pattern Matching for Section Extraction
The application uses a regular expression pattern to capture various Amazon eBook section headings, including:

- Section Start Options: INTRODUCTION, PROLOGUE, PREFACE, FOREWORD, CHAPTER, SECTION, PART, BOOK, with optional numbering.
- Section End Options: END, CONCLUSION, EPILOGUE, APPENDIX, NEXT, with optional numbering.
The flexible pattern matching allows the application to handle diverse eBook formatting styles.


## File Structure
book-publisher/
```text 
├── data/
│   └── [Book Folders with HTML and Images]
├── utils/
│   ├── html_reader.py            # Functions for loading HTML content
│   ├── text_processing.py        # Functions for text processing, chunking, summarization, rephrasing
│   └── embedding_storage.py      # Functions for storing embeddings in Qdrant
├── config.py                     # Configuration for Qdrant connection
├── main.py                       # Main application file with Gradio interface
└── README.md                     # Project documentation
```

## Acknowledgments
Gradio - Interactive UI for the application.
OpenAI - Language model API for text processing.



