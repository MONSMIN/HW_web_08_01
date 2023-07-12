import argparse
import src.connect
from src.models import Author, Quote


def search_quotes_by_author(author_name):
    author = Author.objects(fullname=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        return [quote.quote for quote in quotes]
    else:
        return []

def search_quotes_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return [quote.quote for quote in quotes]

def search_quotes_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return [quote.quote for quote in quotes]

def run_search(command, value):
    if command == "name":
        quotes = search_quotes_by_author(value)
        print("\n".join(quotes).encode('utf-8'))
    elif command == "tag":
        quotes = search_quotes_by_tag(value)
        print("\n".join(quotes).encode('utf-8'))
    elif command == "tags":
        quotes = search_quotes_by_tags(value)
        print("\n".join(quotes).encode('utf-8'))
    else:
        print("Невідома команда. Спробуйте ще раз.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['name', 'tag', 'tags'], help='Команда пошуку: name, tag, або tags')
    parser.add_argument('value', help='Значення для пошуку')
    args = parser.parse_args()

    run_search(args.command, args.value)
