# -*- coding: utf-8 -*-
# To You Alone Oh Father, I commit myself
import os

class FileSystem():


    """
    File system
    sets the actual file name (folders are treated as files)
    sets the file type
    returns the encoding
    returns the data
    """


    def __init__(self):


        super.__self__
        self.Default_LOCATION = "C:/Program Files (x86)/Deuteronomy Works/Peter/Server"
        self._actual_file = ''
        self._file_extension = ''


    def _getFileName(self, requested_file):


        # first split to reveal query if any
        # query will be in the second one without the '?' if any
        splits = requested_file.split('?')

        # whether or not is a query we are still taken the file only
        self._actual_file = splits[0]

        # the extension will be in the last one
        split = self._actual_file.split('.')
        self._file_extension = split[-1]


    def search(self, file):


        # call to find actual file name
        self._getFileName(file)
 
        # this are the steps we'll use and depth we have to go
        steps = self._actual_file.split('/')
        depth = len(steps)

        # try to open the file
        try:

            # try to find oepn file here
            no = 1
            folders = os.listdir(self.Default_LOCATION)
            for item in folders:
                if steps[no] == '':
                    pass
                elif item == steps[no]:
                    pass

            # status code found
            return 302

        except:

            # status code not found
            return 404
