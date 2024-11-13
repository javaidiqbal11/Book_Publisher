# Book Publisher Amazon 
The Book Publisher is a Python application that processes Amazon eBook content by extracting, summarizing, and rephrasing introductory sections. This application leverages Gradio for an interactive interface, Qdrant for embedding storage, and OpenAI models for text processing.

---
## Features
- Automatic Book Content Selection: Selects eBook HTML content from available files in the data folder.
- Content Summarization: Summarizes the introductory content of eBooks.
- Content Rephrasing: Rephrases sections of eBook content.
- Embedding Storage: Stores content embeddings in Qdrant for future retrieval and analysis.
- Pattern Matching: Extracts specific sections using flexible pattern matching to recognize a variety of eBook heading styles.

