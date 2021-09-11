from flask import jsonify

frontend_url = 'http://localhost:5500'

def make_response(data={}, status=200):
    '''
        - Make a resionable response with header
        - status default is 200 mean ok
    '''
    res = jsonify(data)
    res.headers.add('Access-Control-Allow-Origin', frontend_url)
    res.headers.add('Content-Type', 'application/json')
    res.headers.add('Accept', 'application/json')
    res.headers.add('Access-Control-Allow-Credentials', 'true')
    return res