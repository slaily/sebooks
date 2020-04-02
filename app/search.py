from app.utils import query_solr


def search_books_by_title(title):
    query_string = ''.join(['name', ':', title])

    return query_solr(query_string)
