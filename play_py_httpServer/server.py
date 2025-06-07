import socket

def server():
    host = socket.gethostname()
    port = 5000
    # create a new socket
    server_socket = socket.socket()
    server_socket.bind((host,port))
    # at most listen from 2 clients
    server_socket.listen(2)
    connect_skt,client_addr=server_socket.accept()
    print("connection from:"+ str(client_addr))
    #continuously tackle with the requests sent from clients
    while True:
        #set the maximun bytes that the server can receive at one time
        data = connect_skt.recv(1024).decode()
        if not data:
            break
        print("from client:"+str(data))
        response=input("->")
        connect_skt.send(response)
    connect_skt.close()

if __name__=='__main__':
    server()
