# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:52:27 2018

@author: Amoh - Gyebi Godwin
"""

import socketserver
from headers import Header

class Peter(socketserver.BaseRequestHandler):
    """
    The Peter Server Implementation
    
    Source copied from python documentation
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data)
        # mine
        peter = Header()
        resp = Header.computeResponse(peter)
        self.request.sendall(resp)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), Peter) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()