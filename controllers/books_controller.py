from flask import Flask, render_template, request, Blueprint, redirect
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository


# - First create a blueprint

books_blueprint = Blueprint("books", __name__)

# INDEX
# GET '/books'

# - To get books we can use a blueprint which allows us to add multiple paths to our books route on the app. I.e extensions to /books such as /books/new.html etc. Books is the "index" of our route??

# - This blueprint for the route /"books" on the app. It returns the value of all_books which is a select all SQL query and for the books/index.html file in the templates

@books_blueprint.route("/books")
def books():

    # - Python converted SQL query
    books = book_repository.select_all()
    # - Return page with result of all books so we can loop through the data
    return render_template("books/index.html", all_books = books)

# NEW
# GET '/books/new'

@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)



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

# - Here we define the action (also a route) we want to take on a book by its ID


@books_blueprint.route("/books/<id>/delete", methods=["POST"])
# - Ensure we give delete book id as an argument otherwise will get a TypeError
def delete_book(id):
    # - Python SQL query to delete by id
    book_repository.delete(id)
    # - refresh the page on books after we have deleted the item
    return redirect("/books")
    # - On index.html within books we create a POST form and button linked to action a delete from the page

