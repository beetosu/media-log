from flask import Flask, render_template
import books

bookDict = books.create()
app = Flask(__name__)

@app.route("/book/<bookId>")
def hello_world(bookId):
    return render_template('book.html', book=bookDict[bookId])