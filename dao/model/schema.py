
from setup_db import db
from marshmallow import Schema, fields

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()



class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)





