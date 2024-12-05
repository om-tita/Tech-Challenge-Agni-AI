import streamlit as st
import openai
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to summarize text using OpenAI GPT
def summarize_text(text, summary_length):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': f'Summarize the following text into a {summary_length} summary:\n{text}'}
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit app layout
st.title('AI Text Summarizer')

# User input section
input_type = st.radio('Select input type:', ['Paste Text', 'Upload .txt File'])

if input_type == 'Paste Text':
    user_input = st.text_area('Paste your text here:')
else:
    uploaded_file = st.file_uploader('Upload a .txt file', type='txt')
    if uploaded_file is not None:
        user_input = uploaded_file.read().decode('utf-8')

# Summary length selection
summary_length = st.selectbox('Select summary length:', ['short', 'medium', 'long'])

# Summarization button
if st.button('Summarize'):
    if user_input:
        with st.spinner('Summarizing...'):
            summary = summarize_text(user_input, summary_length)
        st.subheader('Summary:')
        st.write(summary)
    else:
        st.error('Please provide text to summarize.')