from typing import List

from dao.model.models import Movie
from dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> List[Movie]:
        return self.movie_dao.get_all_movies()

    def get_movie_by(self, id=None, director_id=None, genre_id=None, year=None):

        if id is not None and director_id is not None and genre_id is not None and year is not None:
            return self.movie_dao.get_movie_by_many_filters(
                id=id,
                director_id=director_id,
                genre_id=genre_id,
                year=year
            )

        if director_id is not None:
            return self.movie_dao.get_movie_by_director_id(director_id)

        elif genre_id is not None:
            return self.movie_dao.get_movie_by_genre_id(genre_id)

        elif year is not None:
            return self.movie_dao.get_movie_by_year(year)

        elif id is not None:
            return self.movie_dao.get_movie_by_id(id)

        else:
            return []

    def add_file(self, data) -> None:
        self.movie_dao.create(**data)

    def update_film(self, data) -> None:
        self.movie_dao.update(**data)

    def delete_film_by_id(self, id) -> None:
        self.movie_dao.delete(id)
