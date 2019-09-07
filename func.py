import threading
import json
import os
import subprocess
import base64
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class Switcher(QObject):

    """
    """

    def __init__(self, setts):
        QObject.__init__(self)
        self.setts = setts
        self.settings = []
        self.server = []
        self.passcode = ""
        self.port = 0
        self.web_sProc = 0
        self.mysql_sProc = 0

    log = pyqtSignal(list, arguments=['logger'])
    sendStatusInfo = pyqtSignal(list, arguments=['sendStatus'])
    changedPort = pyqtSignal(str, arguments=['changed_port'])

    @pyqtSlot()
    def getStatus(self):

        ini_stat = threading.Thread(target=self.sendStatus)
        ini_stat.daemon = True
        ini_stat.start()

    def sendStatus(self):

        self.passcode = self.setts.passcode
        self.server = self.setts.server
        print(self.setts.server)
        self.port = self.setts.port
        self.sendStatusInfo.emit(self.setts.server)

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
        self.setts.server[index]['status'] = new_sts

    def logger(self, index, message):

        self.log.emit([index, message])

    @pyqtSlot(str)
    def change_port(self, new_port):
        port_thread = threading.Thread(target=self._change_port,
                                       args=[new_port])
        port_thread.daemon = True
        port_thread.start()

    def _change_port(self, new_port):
        # changes the port
        self.setts.server[0]["port"] = int(new_port)
        # update UI code also
        self.changed_port(new_port)

    def changed_port(self, new_port):
        # send to Qml layer
        self.changedPort.emit(new_port)
