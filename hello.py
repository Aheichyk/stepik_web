def process_http_request(environ, start_response):
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
    ]
    start_response(status, response_headers)
    body = [(i + '\n') for i in environ['QUERY_STRING'].split('&')]
    return body