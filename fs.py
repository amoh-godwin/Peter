# -*- coding: utf-8 -*-
# To You Alone Oh Father, I commit myself
import os
import chardet

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
        self._no = 0
        self._steps = []
        self._depth = 0
        self.SCRIPTS_LOCATION = "C:/Program Files (x86)/Deuteronomy Works/Peter/_scripts"
        self._file_extension = ''
        self.data = ''
        self.encoding = ''
        self.contentLength = 0


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
        self._steps = self._actual_file.split('/')

        # some clean ups
        del self._steps[0]

        # the depth of the path
        self._depth = len(self._steps)

        # try to open the file
        try:

            # try to find oepn file here
            # INITIALISE THE COUNTER
            self._no = 0

            if self._steps[self._no] == '':
                self._to_list(self.Default_LOCATION)

            else:

                # call
                folders = os.listdir(self.Default_LOCATION)
                if self._steps[self._no] in folders:

                    # if that step is here then we continue
                    item = self.Default_LOCATION + '/' + self._steps[self._no]

                    if self._is_dir(item):

                        # check if blank ''
                        self._is_blank(item)

                    else:

                        # its a file return it
                        self._data(item)

                else:

                    # will couldn't find the file in the nest
                    print('see the 404')
                    pass

            # status code found
            return 302

        except:

            # status code not found
            return 404


    def _crawl(self, path, needle):
        folders = os.listdir(path)
        if needle in folders:

            # make new path
            item = path + '/' + needle

            # find if is file or dir
            if self._is_dir(item):

                # continue crawling is a dir
                self._is_blank(item)

            else:

                # return, it is a file
                # data will be ready in self.data
                self._data(item)
            
        else:
            
            # we couldn't find it means we have ended
            print('another error 404')

    def _is_blank(self, path):

        # depths
        self._no += 1

        # check if the current no is not blank
        if self._no == self._depth:
            
            self._to_list(path)

        elif self._steps[self._no] != '':

            # crawl again
            # needle is second param
            self._crawl(path, self._steps[self._no])

        else:

            # to dir listing or index.html
            self._to_list(path + '/' + self._steps[self._no])


    def _is_dir(self, path):
        try:
            os.listdir(path)
            return True
        except:
            return False


    def _to_list(self, path):


        """
        checks whether this particular path has an index file in it
        or Peter should go ahead and check the .htaccess for listing perm.
        """


        files = os.listdir(path)

        if 'index.php' in files:

            # call self._data to handle
            self._data(path + '/index.php')

        elif 'index.html' in files:

            # call self.data to handle
            self._data(path + '/index.html')

        else:
            # htacces or just go ahead to list dir
            self._data(self.SCRIPTS_LOCATION + '/dir.html' )


    def _data(self, file):

        with open(file, 'rb') as bbin:
            read = bbin.read()

            # set length of the content
            self.contentlength = len(read)

        detection = chardet.detect(read)

        if detection['confidence'] > 0.99:
            self.encoding = detection['encoding']

        else:
            self.encoding = 'ascii'

        self.data = read.decode(self.encoding)

        return
