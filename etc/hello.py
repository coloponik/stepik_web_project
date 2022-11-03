pythonpath = '/home/user1/web'
bind = '0.0.0.0:8080'
def application(environ, start_response):
    data = b'Hello, World!\n';
    status = '200 OK';
    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, headers)
    return iter([data])