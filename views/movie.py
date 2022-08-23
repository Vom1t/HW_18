# Вьюшка для фильмов

from flask import request
from flask_restx import Resource, Namespace

from dao.model.schema import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema(many=True)


@movie_ns.route('/')
# @movie_ns.param('director_id')
# @movie_ns.param('genre_id')
# @movie_ns.param('year')
class MovieView(Resource):
    def get(self):
        """
        Получение всех фильмов
        :return:
        """

        # Метод, который достанет из бд все сущности
        if director_id := request.args.get('director_id'):
            return movie_schema.dump(movie_service.get_movie_by(director_id=director_id)), 200
        elif genre_id := request.args.get('genre_id'):
            return movie_schema.dump(movie_service.get_movie_by(genre_id=genre_id)), 200
        elif year := request.args.get('year'):
            return movie_schema.dump(movie_service.get_movie_by(year=year)), 200
        else:
            return movie_schema.dump(movie_service.get_movies()), 200

    def post(self):
        """
        Добавление нового фильма
        :return:
        """
        # Метод, который положит запись в БД
        movie_service.add_file(request.json)

        return "", 201


@movie_ns.route('/<int:movie_id>/')
class MoviesView(Resource):
    def get(self, movie_id: int):
        """
        Получение фильма по id
        :return:
        """

        # Метод, который достанет из бд все сущности по id

        return movie_schema.dump([movie_service.get_movie_by(movie_id)]), 200

    def put(self, movie_id: int):
        """
        Изменение фильма по id
        :return:
        """
        # Метод, который изменит запись в БД
        movie_service.update_film(request.json)

        return "", 201

    def delete(self, movie_id: int):
        """
        Удаления фильма по id
        :return:
        """

        # Метод, который изменит запись в БД
        movie_service.delete_film_by_id(movie_id)
        return "", 201