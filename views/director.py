# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace

director_ns = Namespace('director')


@director_ns.route('/')
@director_ns.param('director_id')
@director_ns.param('director_id')
@director_ns.param('year')
class DirectorsView(Resource):
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


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id: int):
        """
        Получение фильма по id
        :return:
        """

        # Метод, который достанет из бд все сущности по id

        return "", 200

    def put(self, director_id: int):
        """
        Изменение фильма по id
        :return:
        """

        # Метод, который изменит запись в БД
        return "", 201

    def delete(self, director_id: int):
        """
        Удаления фильма по id
        :return:
        """

        # Метод, который изменит запись в БД
        return "", 201