import openai

class TextSummarizer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def summarize(self, text, summary_length='medium'):
        prompt = self._create_prompt(text, summary_length)
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['choices'][0]['message']['content']

    def _create_prompt(self, text, summary_length):
        length_map = {
            'short': 'Please summarize the following text in a few sentences:',
            'medium': 'Please provide a concise summary of the following text:',
            'long': 'Please summarize the following text in detail:'
        }
        prompt = length_map.get(summary_length, length_map['medium']) + '\n\n' + text
        return prompt