from datetime import datetime

import requests
from bs4 import BeautifulSoup

from webtrack.webapp.db import db
from webtrack.webapp.news.models import News


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_="list-recent-posts").find_all('li')
        result = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time')['datetime']
            try:
                published = datetime.strptime(published, "%Y-%m-%d")
            except ValueError:
                print(published)
                published = datetime.now()
            save_news(title, url, published)


def save_news(title, url, published):
    news_exist = News.query.filter(News.url == url).count()
    print(news_exist)
    if not news_exist:
        news_news = News(title=title, url=url, published=published)
        db.session.add(news_news)
        db.session.commit()
