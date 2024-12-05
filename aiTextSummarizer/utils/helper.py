import os
import openai

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def summarize_text(text, summary_length='medium'):
    """
    Summarizes the given text using OpenAI's GPT model.
    
    Parameters:
    - text (str): The text to summarize.
    - summary_length (str): The desired length of the summary ('short', 'medium', 'long').
    
    Returns:
    - str: The summarized text.
    """
    length_mapping = {
        'short': 50,
        'medium': 100,
        'long': 150
    }
    max_tokens = length_mapping.get(summary_length, 100)
    
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': f'Summarize the following text in {summary_length} length:\n\n{text}'}
        ],
        max_tokens=max_tokens
    )
    
    return response['choices'][0]['message']['content']


def read_text_file(file_path):
    """
    Reads text from a .txt file.
    
    Parameters:
    - file_path (str): The path to the .txt file.
    
    Returns:
    - str: The content of the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()