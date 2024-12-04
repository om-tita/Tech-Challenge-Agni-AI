import streamlit as st
from utils.helper import load_text_file
from models.summarizer import summarize_text

# Title of the app
st.title('AI Text Summarizer')

# User input section
st.header('Paste your text or upload a .txt file')
text_input = st.text_area('Enter text here')
file_upload = st.file_uploader('Or upload a .txt file', type=['txt'])

if file_upload is not None:
    text_input = load_text_file(file_upload)

# Summary length selection
summary_length = st.selectbox('Select summary length', ['Short', 'Medium', 'Long'])

# Summarization button
if st.button('Summarize'):
    if text_input:
        summary = summarize_text(text_input, summary_length)
        st.subheader('Summary')
        st.write(summary)
    else:
        st.warning('Please enter text or upload a file to summarize.')