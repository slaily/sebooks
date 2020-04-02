import requests

from flask import Blueprint

from app.utils import extract_query
from app.search import search_books_by_title


main = Blueprint('main', __name__)


@main.route('/search')
def search():
    query = search_books_by_title('The')
    books_kwargs = extract_query(query)

    return books_kwargs
