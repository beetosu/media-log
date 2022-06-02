from flask import Flask, render_template
import books

bookDict = books.create()
app = Flask(__name__)

@app.template_filter()
def format_percentage(value, outOf):
    percent = (value / outOf) * 100
    return f"{round(percent, 1)}%"

@app.route("/book/<bookId>")
def hello_world(bookId):
    return render_template('book.html', book=bookDict[bookId])