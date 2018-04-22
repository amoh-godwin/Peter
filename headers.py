# -*- coding: utf-8 -*-

class Header():
    
    """
    This handles the calculation of the header variables.
    
    Apart from the computeResponse function, every one of the functions
    are returning a string and only a string
    The computeResponse output should be a byte of-course
    
    """
    
    
    def __init__(self):
        super.__self__
        self.content_length = "0"

    def computeResponse(self):
        # Todo: use these real varibbles
        #return status, content_length, content_type, date, server
        return bytes('HTTP/1.0 200 OK\nContent-Length: 414\r\nContent-type: text/html; charset=utf-8\r\nDate: Sun, 22 Apr 2018 15:45:36 GMT\r\nServer: SimpleHTTP/0.6 Python/3.6.1\n\n<!Doctype html><html>LoveGod</html>', 'utf-8')

    def _contentLength(self):
        self.content_length = "500"
        return self.content_length
    