import os
import streamlit as st


def load_text_file(uploaded_file):
    """Load text from a .txt file."""
    if uploaded_file is not None:
        return uploaded_file.read().decode('utf-8')
    return None


def get_summary_length_option():
    """Get the user's choice for summary length."""
    options = ['Short', 'Medium', 'Long']
    choice = st.selectbox('Select Summary Length:', options)
    return choice


def display_summary(summary):
    """Display the summarized text in the app."""
    st.subheader('Summary')
    st.write(summary)


def show_error_message(message):
    """Display an error message in the app."""
    st.error(message)
