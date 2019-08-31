import threading
import json
import subprocess
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class Switcher(QObject):

    """
    """

    def __init__(self):
        QObject.__init__(self)
        self.parent_folder = "C:/Deuteronomy Works/Peter/settings"
        self.status_file = "/dicdlkcdkdkjfsd.settings"
        self.server = []
        self.service = ['wampstackApache', 'wampstackApache']

    log = pyqtSignal(list, arguments=['logger'])
    sendStatusInfo = pyqtSignal(list, arguments=['sendStatus'])

    @pyqtSlot()
    def getStatus(self):

        ini_stat = threading.Thread(target=self.sendStatus)
        ini_stat.daemon = True
        ini_stat.start()

    def sendStatus(self):

        file_path = self.parent_folder + self.status_file

        with open(file_path, mode="r", encoding="utf-8") as sets_file:
            data = json.load(sets_file)
        self.server = data
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

    def _startService(self, index):
        cmd = "NET START " + self.service[index]
        subprocess.run(cmd)

    def _stopService(self, index):
        cmd = "NET STOP " + self.service[index]
        subprocess.run(cmd)

    def _updateStatus(self, index, new_sts):
        self.server[index]['status'] = new_sts

    def logger(self, index, message):

        self.log.emit([index, message])

    def save_file(self):
        file_path = self.parent_folder + self.status_file

        with open(file_path, mode="w", encoding="utf-8") as sets_file:
            json.dump(self.server, sets_file, indent=4)

