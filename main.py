import openai
from dotenv import load_dotenv
import os
import config
import re
from bs4 import BeautifulSoup

# Load environment variables, including the OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the chunk_text function
def chunk_text(text, chunk_size=500):
    
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

# Define the generate_embedding function with the correct syntax
def generate_embedding(text):
    response = openai.embeddings.create(
        input=[text],  # input should be a list even if it contains only one text
        model="text-embedding-ada-002"
    )
    embedding = response.data[0].embedding  # Access the embedding directly
    return embedding

# Define the function to extract content from HTML with the chunk from Chapter 1 to Chapter 2
def extract_key_section(text):

   
    # pattern = re.compile(
    #     r"\b("
    #     r"(INTRODUCTION|CHAPTER 1.|introduction|INTRODUCTION I|Chapter 1|CHAPTER I|Section 1|I)"
    #     r")\b(.*?)(?=\b("
    #     r"OTHER HEADING|CHAPTER 2.|other heading|OTHER SECTION|Chapter 2|CHAPTER II|Section 2|II"
    #     r")\b|\Z)",
    #     re.DOTALL | re.IGNORECASE
    # )


    # Updated pattern to match different possible naming conventions for start and end sections
    pattern = re.compile(
        r"\b("
        r"(INTRODUCTION|CHAPTER 1|CHAPTER I|CHAPTER ONE|PROLOGUE|FOREWORD|PREFACE|introduction|Introduction|Prologue|Foreword|Preface|Section 1|I|Part 1|PART ONE|First Section|Start)"
        r")\b(.*?)(?=\b("
        r"CONCLUSION|AFTERWORD|EPILOGUE|END|CHAPTER 2|CHAPTER II|CHAPTER TWO|OTHER HEADING|SECTION 2|II|Part 2|PART TWO|Second Section|Next Chapter|Finish"
        r")\b|\Z)",
        re.DOTALL | re.IGNORECASE
    )


    # Search for the first match with priority on Chapter 1
    match = pattern.search(text)
    selected_text = match.group(0) if match else text  # Use match or fallback to entire text

    return selected_text

# Summarization function
def summarize_text(html_file):
    section_content = extract_key_section(html_file)
    focus_text = "Summarize the following section:\n\n" + section_content

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": focus_text}],
        max_tokens=config.MAX_TOKENS
    )
    return response.choices[0].message.content.strip()


def rephrase_text(html_file, target_word_count=5000):
    rephrased_text = ""
    section_content = extract_key_section(html_file)

    while len(rephrased_text.split()) < target_word_count:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": f"Rephrase and expand this text to help reach a total of {target_word_count} words:\n\n{section_content}"
                }
            ],
            max_tokens=config.MAX_TOKENS
        )

        # Append each rephrased chunk to the final text
        new_content = response.choices[0].message.content.strip()
        rephrased_text += " " + new_content

        # Stop if we have reached or exceeded the target word count
        if len(rephrased_text.split()) >= target_word_count:
            break

    # Trim to the exact target word count if it exceeds
    rephrased_words = rephrased_text.split()
    if len(rephrased_words) > target_word_count:
        rephrased_text = ' '.join(rephrased_words[:target_word_count])

    return rephrased_text.strip()


