from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

from utils import get_key_from_config


def extract_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')  # Assuming the text is in paragraph tags. Change based on actual structure.
    article_content = ' '.join([para.text for para in paragraphs])
    return article_content


def extract_news_by_topic(topic):
    newsapi_key = get_key_from_config("newsapi_key")
    date_today = datetime.today().strftime('%Y-%m-%d')
    date_a_week_ago = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    newsapi_config = ('https://newsapi.org/v2/everything?'
                      f'q="{topic}"&'
                      f'from={date_today}&'
                      f'to={date_a_week_ago}&'
                      'sortBy=popularity&'
                      f'apiKey={newsapi_key}')
    response = requests.get(newsapi_config)
    return response.json()
