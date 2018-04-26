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
        self._no = 0
        self._steps = []
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
        self._steps = self._actual_file.split('/')

        # some clean ups
        del self._steps[0]

        # the depth of the path
        depth = len(self._steps)

        # try to open the file
        try:

            # try to find oepn file here
            # INITIALISE THE COUNTER
            self._no = 0

            if self._steps[self._no] == '':
                self._no += 1
                print('blank')

            else:

                # call
                folders = os.listdir(self.Default_LOCATION)
                if self._steps[self._no] in folders:

                    # if that step is here then we continue
                    item = self.Default_LOCATION + '/' + self._steps[self._no]

                    if self._is_dir(item):
                        print('is dir')
                        
                        
                        self._is_blank(item)

                        """# the depth
                        no += 1

                        # check if the current no is not blank
                        if steps[no] != '':

                            print('lets crawl')
                            # crawl again
                            # needle is second param
                            self._crawl(item, steps[no])

                        else:

                            # to dir listing or index.html
                            print('listing')
                            pass"""

                    else:
                        # its a file return it
                        print('is file')
                        pass

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
            
            # find if is file or dir
            if self._is_dir(path + '/' + needle):
                # continue crawling is a dir
                print('is a dir')
                self._is_blank(path + '/' + needle)

            else:

                # return, it is a file
                print('is a file')
                pass
            
        else:
            
            # we couldn't find it means we have ended
            print('another error 404')

    def _is_blank(self, path):

        # depths
        self._no += 1

        # check if the current no is not blank
        if self._steps[self._no] != '':

            print('lets crawl')
            # crawl again
            # needle is second param
            self._crawl(path, self._steps[self._no])

        else:

            # to dir listing or index.html
            print('listing')
            pass


    def _is_dir(self, path):
        try:
            os.listdir(path)
            return True
        except:
            return False


fs = FileSystem()
results = FileSystem.search(fs, '/index.html')
print(results)
