# coding: utf-8
import os
import json

_CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
JOURNALS = {}

def load_query_from_file(file_name):
    with open(file_name, 'r') as f:
        try:
            query = json.load(f)
        except ValueError:
            return None

    return query

for f in os.listdir(_CURRENT_DIR + '/templates'):
    issn = f[:9]
    query = load_query_from_file(_CURRENT_DIR + '/templates/%s' % f)

    if query:
        JOURNALS[issn] = query

def load(issn):

    return JOURNALS.get(issn, {})
