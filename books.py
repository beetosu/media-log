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
    url_title = book['title'].lower().split(':')[0].replace(' ', '-')
    if url_title in bookDict:
        url_title += '-' + str(book['year'])
    return url_title

def findLatest(bookDict):
    latest = None
    for k, v in bookDict.items():
        lastUpdate = v['updates'][-1]['date']
        if bookDict.get(latest, v)['updates'][-1]['date'] <= lastUpdate:
            latest = k
    return latest

def create():
    books = {}
    for f in listdir("books"):
        with open(f'books/{f}', encoding='utf-8') as y:
            book = yaml.safe_load(y)
        error = is_well_formed(book)
        if error is not None:
            print(f"{f} is not a well formed yaml file\n{error} was not found.")
            continue
        bookKey = build_id(book, books)
        book['chartX'] = [u['date'].isoformat() for u in book['updates']]
        book['chartY'] = [u['page'] for u in book['updates']]
        book['status'] = book['status'].capitalize()
        if isinstance(book['author'], str):
            book['author'] = [book['author']]
        books[bookKey] = book
        books[bookKey]['url'] = f"/book/{bookKey}" # f"https://media.cwalsh.dev/books/{bookKey}"
    return books