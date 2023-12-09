import socket

_host = socket.gethostbyname(socket.gethostname())
_port = 80

bind = f"{_host}:{_port}"
workers = 4

# run: gunicorn src.main:server
