# -*- coding: utf-8 -*-
# To you alone oh, The Father of Jesus, our Lord. I give Glory. Forever and
# Ever, AAAAAAMEN
import time
import chardet

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
        self._encoding = ''
        self._extension = ''
        self._contentlength = 0
        self.raw_headers = ""
        self.headerPair = {}
        self.data = ''
        self._extMap = {'html': 'text/html', 'htm': 'text/html',
                        'php': 'text/php', 'css': 'text/css',
                        'gif': 'image/gif', 'json': 'application/json'}
        self.functions = {'Host': self._getHost, 'Cookie': self._getCookies}
        self.cookies = {}

    def computeResponse(self):


        """
        Computes the response to be sent back to the browser
        """


        string = ""

        #cookies = {'phpmyadmin': {'phpMyAdmin': "onesdfk", "expires": "Fri, 25-May-2018 09:46:00 GMT", "Max-Age": "2592000", "path": "/phk/jhkl/"},
        # 'user-1': {"user-1": "Jesus", "path": "/path/about/", "expires": "Fri, 25-May-2018 09:46:00 GMT"}}

        string += self._status(200)

        # calculation of the data the we will be sending
        self._data('index.html')

        # return length of the content that we will be sending
        string += self._contentLength()

        # the type of the content that we will be sending
        string += self._contentType()

        # the Godly name of the Server
        string += self.server_name + "\r\n"

        # the cookies that we will be sending
        # will return empty is no cookies are requested
        #cookies_str = self._cookie(cookies)
        string += self._cookie()

        # the actual date this whole event was completed
        string += self._date()

        # this kinda ends the response header
        string += '\n'

        # Here is the actual response data
        string += self.data

        # encode everything and send it to the browser
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


        string = 'Content-Length: '
        string += str(self._contentlength) + '\r\n'
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


    def _contentType(self):


        string = 'Content-Type: '

        # if the encoding detected was ascii use utf-8 instead
        if self._encoding == 'ascii':
            
            # utf-8 handles a lot more
            encoding = 'utf-8'

        # use the encoding that was given by chardet
        else:

            encoding = self._encoding

        # find the extension in the extension map
        if self._extension in self._extMap:

            # add the corresponding format to the string
            string += self._extMap[self._extension] + '; '

        string += 'charset='+encoding

        return string + "\r\n"

    def _data(self, file):


        splits = file.split('.')

        self._extension = splits[1]

        with open(file, 'rb') as bbin:
            read = bbin.read()

            # set length of the content
            self._contentlength = len(read)

        detection = chardet.detect(read)

        if detection['confidence'] > 0.99:
            self._encoding = detection['encoding']

        else:
            self._encoding = 'ascii'

        self.data = read.decode(self._encoding)

        return
