from .models import News
from flask import abort, Blueprint, render_template, current_app
from ..weather import weather_by_city

blueprint = Blueprint('news', __name__)


@blueprint.route("/")
def index():
    page_title = "Новости Python"
    weather = weather_by_city(current_app.config["WEATHER_DEFAULT_CITY"])
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()
    return render_template("news/index.html", page_title=page_title,
                           weather=weather, news_list=news_list)



@blueprint.route("/news/<int:news_id>")
def single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()
    print(my_news)
    if not my_news:
        abort(404)

    return render_template('news/single_news.html',
                           page_title=my_news.title, news=my_news)
