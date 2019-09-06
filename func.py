import threading
import json
import os
import subprocess
import base64
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class Switcher(QObject):

    """
    """

    def __init__(self):
        QObject.__init__(self)
        self.status_file = \
        "3ddb429e2f446edae3406bb9d0799eed7bddda600d9a05fe01d3baaa.settings"
        self.settings = []
        self.server = []
        self.passcode = ""
        self.port = 0
        self.web_sProc = 0
        self.mysql_sProc = 0

    log = pyqtSignal(list, arguments=['logger'])
    sendStatusInfo = pyqtSignal(list, arguments=['sendStatus'])

    @pyqtSlot()
    def getStatus(self):

        ini_stat = threading.Thread(target=self.sendStatus)
        ini_stat.daemon = True
        ini_stat.start()

    def sendStatus(self):

        file_path = self.status_file

        with open(file_path, mode="rb") as sets_file:
            data = self._decrypt(sets_file.read())
            self.settings = json.loads(data)

        self.settings_file = self.settings[0]["settings_file"]
        self.passcode = self.settings[0]["passcode"]
        self.server = self.settings[1]
        print(self.server)
        self.port = self.server[0]["port"]
        self.sendStatusInfo.emit(self.server)

    @pyqtSlot(int)
    def startServer(self, index):

        start_thread = threading.Thread(target=self._startServer, args=[index])
        start_thread.daemon = True
        start_thread.start()

    @pyqtSlot(int)
    def stopServer(self, index):

        stop_thread = threading.Thread(target=self._stopServer, args=[index])
        stop_thread.daemon = True
        stop_thread.start()

    def _startServer(self, index):

        if index == 0:
            self._startWebServer()
        else:
            self._startMySQL()
        self._updateStatus(index, 'Running')
        self.logger(index, 'Running')

    def _stopServer(self, index):

        if index == 0:
            self._stopWebServer()
        else:
            self._stopMySQL()
        self._updateStatus(index, 'Stopped')
        self.logger(index, 'Stopped')

    def _startWebServer(self):
        # cmd = self.server[0]["path"] + " " + str(self.port)
        #print(cmd)
        self.web_sProc = subprocess.Popen([self.server[0]["path"],
                                           str(self.port)],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.STDOUT,
                                           shell=False)
        return True

    def _stopWebServer(self):
        self.web_sProc.kill()
        self.web_sProc = None
        return True

    def _startMySQL(self):
        self.mysql_sProc = subprocess.Popen(
                [self.server[1]["path"]+"mysqld"],
                 stdout=subprocess.PIPE,
                 stderr=subprocess.STDOUT,
                 shell=False)
        print(str(self.mysql_sProc.stdout.read(), 'utf-8'))
        return True

    def _stopMySQL(self):
        self.mysql_sProc.kill()
        self.mysql_sProc = None
        return True

    def _updateStatus(self, index, new_sts):
        self.server[index]['status'] = new_sts

    def logger(self, index, message):

        self.log.emit([index, message])

    def save_file(self):
        file_path = self.settings_file

        self.settings[1] = self.server

        with open(file_path, mode="wb") as sets_file:
            encoded_data = self._encrypt(self.settings)
            sets_file.write(encoded_data)

    def _encrypt(self, data):
        return base64.b64encode(bytes(str(data), 'ascii'))

    def _decrypt(self, data):
        decoded_data = base64.b64decode(data)
        str_data =  str(decoded_data, 'ascii')
        return str_data.replace("'", '"')
