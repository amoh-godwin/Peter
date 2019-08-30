import threading
import json
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class Switcher(QObject):

    """
    """

    def __init__(self):
        QObject.__init__(self)
        self.parent_folder = "C:/Deuteronomy Works/Peter/settings"
        self.status_file = "/dicdlkcdkdkjfsd.settings"
        self.server = {'index': 0, 'name': 'Peter Web Server',
                       'status': "Stopped"}
        self.mysql_server = {'index': 1, 'name': 'MySql Database',
                             'status': "Stopped"}

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
        self.server = data[0]
        self.mysql_server = data[1]
        stats = [data[0], data[1]]
        self.sendStatusInfo.emit(stats)

    @pyqtSlot(int)
    def startServer(self, index):
        start_thread = threading.Thread(target=self._startServer, args=[index])
        start_thread.daemon = True
        start_thread.start()

    def _startServer(self, index):

        self.logger(index, 'Running')

    @pyqtSlot(int)
    def stopServer(self, index):
        stop_thread = threading.Thread(target=self._stopServer, args=[index])
        stop_thread.daemon = True
        stop_thread.start()

    def _stopServer(self, index):

        self.logger(index, 'Stopped')

    def logger(self, index, message):

        self.log.emit([index, message])
