# -*- coding: utf-8 -*-
# To you alone oh, The Father of Jesus, our Lord. I give Glory. Forever and
# Ever, AAAAAAMEN
import time
class Header():
    
    """
    This handles the calculation of the header variables.
    
    Apart from the computeResponse function, every one of the functions
    are returning a string and only a string
    The computeResponse output should be a byte of-course

    """


    def __init__(self):
        super.__self__
        self.server_name = "Server: Peter (Py/3.6.1)"
        self.host = ''
        self.port = 0
        self.content_length = "0"
        self.raw_headers = ""
        self.headerPair = {}
        self.functions = {'Host': self._getHost, 'Cookie': self._getCookies}
        self.cookies = {}

    def computeResponse(self):

        # Todo: use these real varibbles
        #return status, content_length, content_type, date, server

        string = ""
        #cookies = {'phpmyadmin': {'phpMyAdmin': "onesdfk", "expires": "Fri, 25-May-2018 09:46:00 GMT", "Max-Age": "2592000", "path": "/phk/jhkl/"},
        # 'user-1': {"user-1": "Jesus", "path": "/path/about/", "expires": "Fri, 25-May-2018 09:46:00 GMT"}}
        # phpsess = {'PHPSESSID': {'PHPSESSID': "aluer73j023klsafjk190", "path": '/'}}
        
        string += self._status(200)
        string += self._contentLength()
        string += self._contentType()
        string += self._date()
        string += self.server_name + "\r\n"
        #cookies_str = self._cookie(cookies)
        cookies_str = self._cookie()
        string += cookies_str
        string += '\n'
        string += '<!Doctype html><html><h1>Love God</h1></html>'
        return bytes(string, 'utf-8')

    def getRequest(self, header):

        """
        Breaks the req header down to key value pairs and then send them
        to be processed by their corresponding functions.

        """


        # convert from bytes to text
        self.raw_headers = str(header, 'ascii')
        
        # Break into individual lines
        lines = self.raw_headers.split('\r\n')
        
        # Break into key-value pairs
        for pair in lines:

            # for now we are breaking with ': ' to escpace
            # the port no. eg. localhost':'9999
            splits = pair.split(": ")

            # if it was a key-value pair
            if len(splits) > 1:

                # make it a part of the header pair dict
                self.headerPair[splits[0]] = splits[1]

        # loop through the functions we have set and declared
        for func in self.functions:
            
            # key exist in the headers that was sent by client
            if func in self.headerPair:

                # find its corresponding function and set it to a new variable
                function = self.functions[func]

                # run the function with the self and required values
                # This means, every corresponding function must strictly
                # accept a single value
                function(self.headerPair[func])


    def _getHost(self, hostname_str):

        """
        Gets Host and its port

        """


        # for now just put everything as hostname
        # later we break it
        self.host = hostname_str
        print(self.host + " Here")


    def _getCookies(self, cookie_str):

        """
        Breaks the cookie string into individual cookies
        And store them

        """


        # split them in main entries
        splits = cookie_str.split('; ')

        for pair in splits:

            # split into key-value pairs
            pairs = pair.split('=')

            # Add the key-value pairs to the cookies variable
            self.cookies[pairs[0]] = pairs[1]

        print(self.cookies)


    def _status(self, digit):
        string = 'HTTP/1.0 '
        string += str(digit) + " OK\n"
        return string


    def _date(self):
        string_time = "Date: "
        string_time += time.strftime('%a, %d %b %Y %H:%M:%S %Z')
        return string_time + "\r\n"


    def _contentLength(self):

        self.content_length = "500"
        string = 'Content-Length: '
        string += self.content_length + '\r\n'
        return string


    def _cookie(self, cookies=None):


        # set string to empty
        string = ""

        if cookies:

            # cookie's name in cookies multi-dimensional array
            for name in cookies:

                string += "Set-Cookie: "

                # set actual cookie as a "cookie": {}
                cookie = cookies[name]

                # each value that has been listed
                for val in cookie:
                    string += val + "=" + str(cookie[val]) + "; "

                # add the httponly
                string += "HttpOnly\r\n"

        return string


    def _contentType(self, ext=None):
        string = 'Content-Type: '
        if ext:
            pass
        else:
            string += 'text/html; charset=utf-8'
        return string + "\r\n"
