from webtrack.webapp.news.models import News
from flask import Blueprint, render_template, current_app
from webtrack.webapp.weather import weather_by_city

blueprint = Blueprint('news', __name__)


@blueprint.route("/", methods=['POST', 'GET'])
def index():
    page_title = "Новости Python"
    weather = weather_by_city(current_app.config["WEATHER_DEFAULT_CITY"])
    news_list = News.query.order_by(News.published.desc()).all()
    return render_template("news/index.html", page_title=page_title, weather=weather, news_list=news_list)
