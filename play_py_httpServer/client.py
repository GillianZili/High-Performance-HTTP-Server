import socket

def client():
    host = socket.gethostname()
    #since one port can be listened by many services, just register the client and the server at the same port
    port = 5000
    client_socket=socket.socket()
    client_socket.bind((host,port))
    