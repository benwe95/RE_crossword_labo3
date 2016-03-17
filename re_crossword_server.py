# re_crossword_server.py
# Crossword application
# Author: Wery Benoit
# Version: March 16, 2016

import os
from bottle import get, route, run, template, request


@route('/')
def home():
    return template('re_crossword.html')

@get('/answer')
def answer():
    if request.query['answer'].upper() == 'DEEP BLUE':
        return template('re_congratulations.html')
    else:
        return template('re_wrong.html')


run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
