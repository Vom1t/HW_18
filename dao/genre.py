
from dao.model.models import Genre


class GenreDAO:
    def __int__(self, session):
        self.session = session

    def get_all_genres(self):
        return self.session.query(Genre).all()

    def get_genre_by_id(self, id):
        return self.session.query(Genre).filter(Genre.Genre_id==id).one()

