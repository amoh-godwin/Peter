# Thank you Heavenly Father

from subprocess import check_output
import os
import sys

class WinInstall():


    """
    """


    def __init__(self):
        super.__init__
        self.destination = "C:/Deuteronomy/Peter"
        splits = os.path.split(sys.argv[0])
        self.passcode = 'ampofo1'
        self.main = splits[0].replace('/install', '')
        self.copy_files()


    def copy_files(self):


        cmd1 = 'xcopy ' + self.main + '/php' + ' ' + self.destination + '/php/'
        cmd2 = 'xcopy ' + self.main + '/mysql' + ' ' + self.destination + '/mysql/'

        comm1 = cmd1.replace('/', '\\')
        comm2 = cmd2.replace('/', '\\')
        out1 = check_output(comm1 + ' /E /Y', shell=True)
        out2 = check_output(comm2 + ' /E /Y', shell=True)


    def init_mysql(self):


        cmd = self.destination + '/mysql/bin/mysqld --defaults-file="'+ \
        self.destination + '/mysql/my.ini' + '" --initialize-insecure'


    def install_mysql_serv(self):
        
        
        cmd = self.destination + '/mysql/bin/mysqld --install MySQL573 --defaults-file="'+ \
        self.destination + '/mysql/my.ini' + '"'


    def set_pass(self):


        cmd = 'ALTER USER "root"@"localhost" INDENTIFIED BY "'+self.passcode+'"'


WinInstall()