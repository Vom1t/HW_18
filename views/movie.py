# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace

movie_ns = Namespace('movie')


@movie_ns.route('/')
@movie_ns.param('director_id')
@movie_ns.param('genre_id')
@movie_ns.param('year')
class MovieView(Resource):
    def get(self):
        """
        Получение всех фильмов
        :return:
        """

        # Метод, который достанет из бд все сущности

        return "", 200

    def post(self):
        """
        Добавление нового фильма
        :return:
        """

        # Метод, который положит запись в БД
        return "", 201


@movie_ns.route('/<int:movie_id>')
class MoviesView(Resource):
    def get(self, movie_id: int):
        """
        Получение фильма по id
        :return:
        """

        # Метод, который достанет из бд все сущности по id

        return "", 200

    def put(self, movie_id: int):
        """
        Изменение фильма по id
        :return:
        """

        # Метод, который изменит запись в БД
        return "", 201

    def delete(self, movie_id: int):
        """
        Удаления фильма по id
        :return:
        """

        # Метод, который изменит запись в БД
        return "", 201