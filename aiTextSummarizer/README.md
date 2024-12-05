# AI Text Summarizer

## Project Overview
The AI Text Summarizer is a simple web application built with Streamlit that allows users to paste lengthy text or upload a .txt file. The application summarizes the input text into concise key points using OpenAI's GPT language model. This tool provides a quick and easy way to distill essential information from large text inputs.

## Key Features
1. **User Input**: Users can paste text or upload a .txt file.
2. **AI Summarization**: Summarizes text using an AI language model.
3. **Customization**: Users can choose summary length (short, medium, long).
4. **No Database**: All processing is done in memory, with no data storage.

## Tech Stack
- **Framework**: Streamlit
- **AI Model**: OpenAI GPT API 
- **Language**: Python

## Installation
To run this project, you need to have Python installed. You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage
1. Run the application:
   ```bash
   streamlit run main.py
   ```
2. Open your web browser and go to `http://localhost:8501`.
3. Paste your text or upload a .txt file to get the summary.

## Contributing
If you would like to contribute to this project, please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.