from bs4 import BeautifulSoup
import requests

response = requests.get(
    url="https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article in articles:
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0])
                   for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

max_value = max(article_upvotes)
max_index = article_upvotes.index(max_value)
print(article_texts[max_index], article_links[max_index])
