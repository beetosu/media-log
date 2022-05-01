import yaml
from os import listdir

def is_well_formed(book):
    required_entities = ['title', 'author', 'year', 'status']
    for entity in required_entities:
        if not book.get(entity):
            return entity
    if book['status'] == 'completed' and not book.get('rating'):
        return 'rating'

def build_id(book, bookDict):
    url_title = book['title'].replace(' ', '-')
    if url_title in bookDict:
        url_title += '-' + str(book['year'])
    return url_title

def create():
    books = {}
    for f in listdir("books"):
        with open(f'books/{f}') as y:
            book = yaml.safe_load(y)
        error = is_well_formed(book)
        if error is not None:
            print(f"{f} is not a well formed yaml file\n{error} was not found.")
            continue
        bookKey = build_id(book, books)
        books[bookKey] = book
    return books