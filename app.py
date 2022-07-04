from flask import Flask, render_template
import books

bookDict = books.create()
bookLatest = books.findLatest(bookDict)
app = Flask(__name__)

@app.template_filter()
def format_percentage(value, outOf):
    percent = (value / outOf) * 100
    return f"{round(percent, 1)}%"

@app.template_filter()
def format_author(author, authorLst):
    if len(', '.join(authorLst)) > 32:
        return author.split(" ")[1]
    return author

@app.route("/")
def homepage():
    return render_template('homepage.html', book=bookDict[bookLatest])

@app.route("/books")
def get_books():
    return render_template('bookList.html', books=bookDict)

@app.route("/book/latest")
def latest_book():
    return bookDict[bookLatest]

@app.route("/book/<bookId>")
def book_page(bookId):
    return render_template('book.html', book=bookDict[bookId])