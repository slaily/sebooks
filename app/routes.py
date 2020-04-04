import requests

from flask import Blueprint

from app import metrics
from app.utils import extract_query
from app.search import search_books_by_title


main = Blueprint('main', __name__)


@main.route('/search')
@metrics.request_summary.time()
def search():
    query = search_books_by_title('The')
    books_kwargs = extract_query(query)

    return books_kwargs
