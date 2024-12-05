import os
import openai


def load_text_from_file(file_path):
    """Load text from a .txt file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def summarize_text(text, summary_length='medium'):
    """Summarize the given text using OpenAI's GPT API."""
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': f'Summarize the following text into a {summary_length} summary:\n\n{text}'}
        ]
    )
    return response['choices'][0]['message']['content']


def validate_text_input(text):
    """Validate the input text to ensure it is not empty."""
    if not text.strip():
        raise ValueError('Input text cannot be empty.')
    return True
