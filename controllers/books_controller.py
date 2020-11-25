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
# - Showns an html form to create a new book - this SHOWS US THE VIEW! So in our html code we set up what we want to have as inputs on our website so we can link the create method to it and input data

@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)



# CREATE
# POST '/books'

# - This method allows us to create a new book  on the /books route and redirect to it i.e look at the updated view of books once we have input the new book 

@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author = author_repository.select(request.form['author_id'])
    book = Book(title, genre, publisher, author)
    book_repository.save(book)
    return redirect('/books')



# SHOW
# GET '/books/<id>'
@books_blueprint.route("/books/<id>")
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book = book)



# @books_blueprint.route("/books/<id>", methods=["GET"])
# # - Ensure we give delete book id as an argument otherwise will get a TypeError
# def show_book(id):
#     # - Python SQL query to view by id
#     book = book_repository.select(id)
#     # - refresh the page on books after we have deleted the item
#     return render_template("/books/show.html", book = book)



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

