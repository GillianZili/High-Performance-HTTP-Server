import requests
import socket

url = "http://localhost:8080"

# 1. use requests
def use_requests(method):
    if method=="get":
        response = requests.get(url=url)
    elif method =="post":
        response = requests.get(url=url)

    if response.status_code == 200:
        print("Success!")
        print("Response content:", response.text) 
    elif response.status_code == 404:
        print("Not Found.")

# 2. use socket
def use_socket(method):
    # create socket: default: IPv4, TCP socket
    sock=socket.socket()
    sock.connect(("localhost",8080))

    # send request
    if method=="get":
        sock_sendGetRequest(sock)
    elif method=="post":
        sock_sendPostRequest(sock)
    
    # recieve
    response = b""
    while True:
        chunk=sock.recv(1000)
        if not chunk:
            break
        response+=chunk
    print(response.decode())

def sock_sendPostRequest(sock):
    request = (
        "POST / HTTP/1.1\r\n"
        "Host: localhost\r\n"
        "Content-Length: 0\r\n"
        "\r\n"
    )
    sock.send(request.encode("utf-8"))

def sock_sendGetRequest(sock):
    request = b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    sent = 0
    while sent < len(request):
        sent = sent + sock.send(request[sent:])

def main():
    use_socket("get")
    use_socket("post")

if __name__=='__main__':
    main()


