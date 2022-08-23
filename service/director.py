from typing import List

from dao.director import DirectorDAO
from dao.model.models import Movie


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self) -> List[Movie]:
        return self.director_dao.get_all_Directors()

    def get_director_by(self, id):
        return self.director_dao.get_director_by_id(id)
