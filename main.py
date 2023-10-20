from news_service import extract_news_by_topic, extract_article_content
from summary_service import summarize_article


def run_news_summarization_task():
    topic = input("Hi, what topic would you like a summary of ? ")
    news = extract_news_by_topic(topic)
    print(f'Summarizing the top 3 article from {news["totalResults"]} results...')
    print("-----------------------------")
    article_list = news["articles"]
    top_3_article_list = article_list[0:3]  # Assuming articles are ordered by popularity
    for article in top_3_article_list:
        print(f'Title: {article["title"]}')
        article_content = extract_article_content(article['url'])
        article_summary = summarize_article(article_content)
        print(f'Article summary: {article_summary}')
        print(f'Read more: {article["url"]}')
        print("-----------------------------")


if __name__ == "__main__":
    print("Welcome to News Assistant !")
    while True:
        run_news_summarization_task()
        another = input("Would you like to know about another topic ? Type 'Y' to restart. To exit, just press 'Enter'.")
        if another != 'Y':
            break
    print("Bye.")
