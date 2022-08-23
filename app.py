# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.

from flask import Flask
from flask_restx import Api



from config import Config
from setup_db import db
from views.movie import movie_ns
from views.genre import genre_ns
from views.director import director_ns

# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


app = create_app(Config())

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
