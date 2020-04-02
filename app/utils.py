import requests


def query_solr(query_string):
    url = f'http://localhost:8983/solr/books/select?q={query_string}&wt=json'
    response = requests.get(url)

    return response.json()


def extract_query(query):
    kwargs = {
        'metadata': {
            'status': 0,
            'query_time': 0,
            'records': 0,
        },
        'books': []
    }

    if 'response' in query and query['response']['numFound'] > 0:
        # Update the metadata with number of records
        kwargs['metadata']['records'] = query['response']['numFound']
        # Lookup keys for information extraction
        keys_to_extract = (
            'name',
            'author',
            'genre_s',
            'price',
            'pages_i',
        )

        for book_kwargs in query['response']['docs']:
            book = {
                key: value for key, value in book_kwargs.items() if key in keys_to_extract
            }
            kwargs['books'].append(book)

    # Update the metadata with the query metadata
    kwargs['metadata']['status'] = query['responseHeader']['status']
    kwargs['metadata']['query_time'] = query['responseHeader']['QTime']

    return kwargs
