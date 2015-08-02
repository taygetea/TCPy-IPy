import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('http://taygetea.com', 8000))
while 1:
    
