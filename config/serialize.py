from flask_marshmallow import Marshmallow
from config.models import Book

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book