import json
import src.connect
from src.models import Author, Quote



def load_data():
    with open('authors.json', 'r', encoding='utf-8') as authors_file:
        authors_data = json.load(authors_file)

    with open('quotes.json', 'r', encoding='utf-8') as quotes_file:
        quotes_data = json.load(quotes_file)

    for author_data in authors_data:
        author = Author(
            fullname=author_data['fullname'],
            born_date=author_data['born_date'],
            born_location=author_data['born_location'],
            description=author_data['description']
        )
        author.save()

    for quote_data in quotes_data:
        author_name = quote_data['author']
        author = Author.objects(fullname=author_name).first()

        quote = Quote(
            quote=quote_data['quote'],
            author=author,
            tags=quote_data['tags']
        )
        quote.save()


if __name__ == '__main__':
    load_data()
