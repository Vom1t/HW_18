# Вьюшка для режисеров
from flask_restx import Resource, Namespace

from dao.model.schema import DirectorSchema
from implemented import director_service

director_ns = Namespace('director')
director_schema = DirectorSchema(many=True)

@director_ns.route('/')

class DirectorsView(Resource):
    def get(self):
        """
        Получение всех фильмов
        :return:
        """

        # Метод, который достанет из бд все сущности

        return director_schema.dump(director_service.get_directors()), 200


@director_ns.route('/<int:director_id>/')
class DirectorView(Resource):
    def get(self, director_id: int):
        """
        Получение фильма по id
        :return:
        """

        # Метод, который достанет из бд все сущности по id

        return director_schema.dump([director_service.get_director_by_id(director_id)]), 200

