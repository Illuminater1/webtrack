from flask import Flask, render_template


from webapp.model import db, News
from webapp.weather import weather_by_city



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    #разкоментировать при подключении postgre
    db.init_app(app)

    @app.route("/", methods=['POST', 'GET'])
    def index():
        page_title = "Новости Python"
        weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template("index.html", page_title=page_title, weather=weather, news_list=news_list)

    return app