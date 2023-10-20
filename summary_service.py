import requests

from utils import get_key_from_config


def summarize_article(article):
    prompt = " ".join(article.split(' ')[0:3000])  # Limit the article to 3,000 words.
    url = "https://api.openai.com/v1/chat/completions"
    openai_key = get_key_from_config('openai_key')

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_key}"
    }

    data = {  # Request body to ChatGPT. Notice the nested data structure.
        "messages": [
            {
                "role": "system",
                "content": "Summarize the following news article in one paragraph. "
                           "Note that the content is extracted and might be clumsy. "
                           "If the article is not in english, translate it in english."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 1,
        "max_tokens": 4096,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "model": "gpt-3.5-turbo-16k",
        "stream": False
    }

    chatgpt_response = requests.post(url, headers=headers, json=data, timeout=300)
    chatgpt_response_as_dict = chatgpt_response.json()
    summary = chatgpt_response_as_dict.get('choices', [{}])[0].get('message', {}).get('content', '')
    return summary
