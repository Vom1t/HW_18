# Вьюшка для жанров
from flask_restx import Resource, Namespace

from dao.model.schema import GenreSchema
from implemented import genre_service


genre_ns = Namespace('genre')
genre_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):

    def get(self):
        """
        Получение всех жанров
        :return:
        """
        # Метод, который достанет из ДБ все сущности
        return genre_schema.dump(genre_service.get_genres()), 200


@genre_ns.route('/<int:genre_id>/')
class GenresView(Resource):
    def get(self, genre_id: int):
        """
        Получение все жанры по id
        :return:
        """

        # Метод, который достанет из бд все сущности по id
        return genre_schema.dump([genre_service.get_genre_by_id(genre_id)]), 200
