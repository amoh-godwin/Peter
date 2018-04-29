# -*- coding: utf-8 -*-
# To you Alone oh Father, I commit myself

import os
import subprocess

class PHPRunner():


    """
    """


    def __init__(self):
        super.__self__
        self.directory = 'C:/ProgramData/Anaconda3/'
        self.queries = ''
        self.method = ''
        self.redirect_status = 'true'
        self.content_type = ''
        self.file_name = ''
        self.script_name = ''
        self.path_info = '/'
        self.server_name = ''
        self.server_protocol = ''
        self.request_uri = ''
        self.http_host = ''
        self.content_length = 0
        self.echo = ''
        self.get_stmt = "set \"" + self.RedStat() + "\" & set \"" + self.ReqMethod() + \
        "\" & set \"" + self.ContType() + "\" & set \"" + self.ScrFile() + \
        "\" & set \"" + self.ScrName() + "\" & set \"" + self.PathInf() + \
        "/\" & set \"" + self.SerName() + "\" & set \"" + self.Protocol() + \
        "\" & set \"" + self.ReqUri() + "\" & set \"" + self.HTTPHost() + \
        "\" & set \"" + self.QueryStr + "\" & php-cgi"

        self.post_stmt = "set \"" + self.RedStat() + "\" & set \"" + self.ReqMethod() + \
        "\" & set \"" + self.ContType() + "\" & set \"" + self.ScrFile() + \
        "\" & set \"" + self.ScrName() + "\" & set \"" + self.PathInf() + \
        "/\" & set \"" + self.SerName() + "\" & set \"" + self.Protocol() + \
        "\" & set \"" + self.ReqUri() + "\" & set \"" + self.HTTPHost() + \
        "\" & set \"" + self.ConLen() + "\" & echo " + self.Echo() + \
        " | php-cgi"


    def Start(self, file, queries, method ):


        # The functions
        self.RedStat()
        self.ReqMethod()
        self.ContType()
        self.ScrFile()
        self.ScrName()
        self.PathInf()
        self.SerName()
        self.Protocol()
        self.ReqUri()
        self.HTTPHost()
        self.QueryStr()
        self.ConLen()
        self.Echo()

        # run function that make sense only to these methods
        if method == "GET":

            self.content_type = 'text/html'
            self.QueryStr()

        else:

            self.content_type = "application/x-www-form-urlencoded"
            self.Echo()
            self.ConLen()

        # change the directory and file to be safe in testing mode
        os.chdir(self.directory)
        file = 'C:\\index.py'

        # the command
        cmd = "python " + file + " " + queries

        # run the subprocess
        output = subprocess.check_output(cmd, shell=True)

        # return the bin
        return output


    def RedStat(self):

        # make string
        string = "REDIRECT_STATUS=" + self.redirect_status
        return string


    def ReqMethod(self):

        string = "REQUEST_METHOD=" + self.method
        return string


    def ContType(self):

        string = "CONTENT_TYPE=" + self.content_type
        return string


    def ScrFile(self):

        string = "SCRIPT_FILENAME=" + self.file_name
        return string


    def ScrName(self):

        string = "SCRIPT_NAME=" + self.script_name
        return string


    def PathInf(self):

        string = "PATHINFO=" + self.path_info
        return string


    def SerName(self):

        string = "SERVER_NAME=" + self.server_name
        return string


    def Protocol(self):

        string = "SERVER_PROTOCOL=" + self.server_protocol
        return string


    def ReqUri(self):

        string = "REQUEST_URI=" + self.request_uri
        return string


    def HTTPHost(self):

        string = "HTTPHOST=" + self.http_host
        return string


    def QueryStr():

        string = ""
        return string


    def ConLen(self):

        string = "CONTENT_LENGTH=" + self.content_length
        return string


    def Echo(self):
        pass
