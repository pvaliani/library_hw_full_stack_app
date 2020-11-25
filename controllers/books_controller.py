from flask import Flask, render_template, request, Blueprint, redirect
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository


# - First create a blueprint

books_blueprint = Blueprint("books", __name__)

# INDEX
# GET '/books'

# - To get books we can use a blueprint which allows us to add multiple paths to our books route on the app. I.e extensions to /books such as /books/new.html etc. Books is the "index" of our route??

@books_blueprint.route("/books")
def books():

    books = book_repository.select_all()

    return render_template("books/index.html", all_books = books)

# NEW
# GET '/books/new'

# @books_blueprint.route("/books/new", methods=['GET'])
# def new_book():
#     authors = author_repository.select_all()
#     return render_template("books/new.html", all_authors = authors)



# CREATE
# POST '/books'


# SHOW
# GET '/books/<id>'


# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'

