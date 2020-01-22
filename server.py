#  coding: utf-8
import socketserver

# Copyright 2013 Abram Hindle, Eddie Antonio Santos
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/


class MyWebServer(socketserver.BaseRequestHandler):

    #handle function does all the work in this server.
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print ("Got a request of: %s\n" % self.data)
        # print(type(self.client_address))
        # print(self.client_address)
        split_string = self.data.decode('utf-8').split('\r\n')
        request_string = split_string[0]
        command = request_string.split(" ")[0]
        file = request_string.split(" ")[1]

        #Check of method POST/PUT/DELETE (Return 405)
        if command in ["POST", "PUT", "DELETE"]:
            self.request.sendall(bytearray("HTTP/1.1 405 Method Not Allowed",'utf-8'))

        try:
            file = open("www{}".format(file), "r")
        except :
            self.request.sendall(bytearray("HTTP/1.1 404 Not Found",'utf-8'))

        #     self.wfile.write()


        print("FILE: {}".format(command))
        # try:



        # for i in split_string:
        #     print(i, 'Host:' in i)
        self.request.sendall(bytearray("HTTP/1.1 200 OK",'utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = socketserver.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
