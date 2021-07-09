def process_http_request(environ, start_response):
    param = environ.get("QUERY_STRING")
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
    ]
    start_response(status, response_headers)
    return [param.replace('&','\n')]