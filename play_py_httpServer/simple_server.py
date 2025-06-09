from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# HTTPServer can only process one request at a time
# Does not support socket reuse
class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        #constitute the header and body of the response

        #-----header-----
        self.send_header('Content-type','text/html')

        #-----body-----
        with open("static_file.html",'rb') as file:
            html_content=file.read()
        # tell client the length of the notice
        self.send_header('Content-Length', str(len(html_content)))
        self.end_headers()

        self.wfile.write(html_content)
        print("Get requests received successfully.")


    def do_POST(self):
        #parse the Content_Length fields from the http request
        content_length_str=self.headers.get('Content-Length')
        if content_length_str is None:
            self.send_response(400)
            self.end_headers()
            self.wfile.write("missing header from request")
            return
        
        content_length=int(content_length_str)
        data=self.rfile.read(content_length)
        print("received data from client: "+ data.decode('utf-8'))

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"Post requests received successfully.")

def main(): 
    server_address=('',8080)
    httpd=HTTPServer(server_address,MyRequestHandler)

    print('start the server:')
    httpd.serve_forever()

if __name__=='__main__':
    main()

# HTTPServer: parse the requests to fetch the complete data
# handler to route method/url request to corresponding handlers in next layer
# handlers to handle method/url request



        

