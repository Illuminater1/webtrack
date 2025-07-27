from datetime import datetime
from bs4 import BeautifulSoup
import locale
import platform

from webapp.news.parsers.utils import get_html, save_news
from webapp.db import db
from webapp.news.models import News

if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU')

def get_news_snippets():
    html = get_html("https://habr.com/ru/search/?q=python&target_type=posts&order=date")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = (soup.find('div', class_="tm-articles-list").
                    find_All('div', class_='tm-article-snippet tm-article-snippet'))

        for news in all_news:
            title = news.find('a', class_='tm-title__link').text
            url = 'http://habr.com' + news.find('a', class_='tm-title__link')['href']
            published = news.find('time')['title']
            try:
                published = datetime.strptime(published, "%Y-%m-%d, %H:%M")
            except ValueError:
                return datetime.now()
            save_news(title=title, url=url, published=published)
            print(f'{title},\n {url},\n {published}\n')

def get_news_content():
    news_without_text = News.query.filter(News.text.is_(None))
    for news in news_without_text:
        html = get_html(news.url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            news_text = soup.find('div',
                    class_='article-formatted-body article-formatted-body article-formatted-body_version-2').decode_contents()

            if news_text:
                news.text = news_text
                db.session.add(news)
                db.session.commit()
