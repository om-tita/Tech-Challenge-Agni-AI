import os

# Configuration settings for the AI Text Summarizer application

# OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Summary length options
SUMMARY_LENGTH_OPTIONS = {
    'short': 50,
    'medium': 100,
    'long': 200
}

# Default summary length
DEFAULT_SUMMARY_LENGTH = 'medium'

# Streamlit settings
STREAMLIT_TITLE = 'AI Text Summarizer'
STREAMLIT_HEADER = 'Summarize your text quickly and easily!'
