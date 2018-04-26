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

        """
        This is the handler,
        
        handles the request and response from the server
        """


        # self.request is the request from the client
        self.data = self.request.recv(1024).strip()

        # This would be used for logging
        print("{} wrote:".format(self.client_address[0]))

        # The data that the browser came with
        # basically the request handler
        print(self.data)

        # Initialise the header class
        peter = Header()

        # send the request to be proccesed
        Header.getRequest(peter, self.data)

        # This is the response from the server
        # to the browser
        resp = Header.computeResponse(peter)

        # Send the complete data to the browser
        self.request.sendall(resp)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), Peter) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()