import os


def read_text_file(file_path):
    """
    Reads a .txt file and returns its content as a string.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def save_uploaded_file(uploaded_file, save_path):
    """
    Saves the uploaded file to the specified path.
    """
    with open(save_path, 'wb') as file:
        file.write(uploaded_file.getbuffer())


def is_text_file(file_name):
    """
    Checks if the uploaded file is a .txt file.
    """
    return file_name.endswith('.txt')
