import streamlit as st
from utils.helper import summarize_text

st.title('AI Text Summarizer')

st.write('Paste your text below or upload a .txt file to summarize it.')

text_input = st.text_area('Input Text')

uploaded_file = st.file_uploader('Upload a .txt file', type='txt')
if uploaded_file is not None:
    text_input = uploaded_file.read().decode('utf-8')

summary_length = st.selectbox('Select Summary Length', ['Short', 'Medium', 'Long'])

if st.button('Summarize'):
    if text_input:
        summary = summarize_text(text_input, summary_length)
        st.subheader('Summary')
        st.write(summary)
    else:
        st.error('Please provide text input or upload a file.')