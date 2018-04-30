# -*- coding: utf-8 -*-
# To you Alone, oh God. I commit myself
import re
class PHPHeader():


    def __init__(self):
        super.__self__
        self.clean_map = ['Content-type: ']


    def computeHeader(self, headers):


        # break on (\r\n)
        splits = headers.split('\r\n')

        # string
        string = ""

        # clean it up now
        for header in splits:
            for item in self.clean_map:
                regex = '^' + item + '.*'
                if re.findall(regex, header):
                    splits.remove(header)
        
        for header in splits:
            string += header + '\r\n'
        
        return string
