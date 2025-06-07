import requests
import socket

url = "http://localhost:8080"

# 1. use requests
# response = requests.get(url=url)
# if response.status_code == 200:
#     print("Success!")
#     print("Response content:", response.text) 
# elif response.status_code == 404:
#     print("Not Found.")

# 2. use socket
# default: IPv4, TCP socket
skt=socket.socket()
skt.connect(("localhost",8080))

# 2.1 POST request
# request = (
#     "POST / HTTP/1.1\r\n"
#     "Host: localhost\r\n"
#     f"Content-Length: 0\r\n"
#     "\r\n"
# )
# skt.send(request.encode("utf-8"))

# 2.2 GET request
request = b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
sent = 0
while sent < len(request):
    sent += sent + skt.send(request[sent:])

response = b""
while True:
    chunk=skt.recv(1000)
    if not chunk:
        break
    response+=chunk
skt.close()
print(response.decode())


