from flask import Blueprint, current_app, request, jsonify
from config.models import Book
from config.serialize import BookSchema



bp_books = Blueprint('books',__name__)

@bp_books.route('/mostrar', methods = ['GET'])
def mostrar():
   bs = BookSchema(many = True)
   result = Book.query.all()
   return bs.jsonify(result),200



@bp_books.route('/cadastrar', methods = ['POST'])
def cadastrar():
   bs = BookSchema()
   book, error = bs.load(request.json)
   current_app.db.session.add(book)
   current_app.db.session.commit()
   return bs.jsonify(book), 201



@bp_books.route('/deletar/<id>', methods = ['DELETE'])
def deletar(id):
    Book.query.filter(Book.id == id).delete()
    current_app.db.session.commit()
    return jsonify('Objeto deletado!!!')


   

@bp_books.route('/editar', methods = ['PUT'])
def editar():
    bs = BookSchema()
    book = request.json
    print (book)
    query = Book.query.filter(Book.id == book['id'])
    query.update(book)
    current_app.db.session.commit()
    return bs.jsonify(query.first())
