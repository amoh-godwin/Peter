import threading
import json
import subprocess
import base64
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class Switcher(QObject):

    """
    """

    def __init__(self):
        QObject.__init__(self)
        self.parent_folder = "C:/Deuteronomy Works/Peter/settings"
        self.status_file = \
        "/3ddb429e2f446edae3406bb9d0799eed7bddda600d9a05fe01d3baaa.settings"
        self.server = [{"index": 0, "name": "Peter Web Server", "status": "Stopped"},
                       {"index": 1, "name": "MySQL Database", "status": "Stopped"}]

    log = pyqtSignal(list, arguments=['logger'])
    sendStatusInfo = pyqtSignal(list, arguments=['sendStatus'])

    @pyqtSlot()
    def getStatus(self):

        ini_stat = threading.Thread(target=self.sendStatus)
        ini_stat.daemon = True
        ini_stat.start()

    def sendStatus(self):

        file_path = self.parent_folder + self.status_file

        with open(file_path, mode="rb") as sets_file:
            decoded = base64.b64decode(sets_file.read())
            data = str(decoded, 'ascii').replace("'", '"')
            info = json.loads(data)

        self.server = info
        stats = self.server
        self.sendStatusInfo.emit(stats)

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

        # self._startService(index)
        self._updateStatus(index, 'Running')
        self.logger(index, 'Running')

    def _stopServer(self, index):

        # self._stopService(index)
        self._updateStatus(index, 'Stopped')
        self.logger(index, 'Stopped')

    def _updateStatus(self, index, new_sts):
        self.server[index]['status'] = new_sts

    def logger(self, index, message):

        self.log.emit([index, message])

    def save_file(self):
        file_path = self.parent_folder + self.status_file

        with open(file_path, mode="wb") as sets_file:
            encoded_data = base64.b64encode(bytes(str(self.server), 'ascii'))
            sets_file.write(encoded_data)

