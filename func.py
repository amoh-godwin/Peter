import threading
import subprocess
import os

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
import psutil

from settings import Sets

setts = Sets()

class Switcher(QObject):

    """
    """

    def __init__(self):
        QObject.__init__(self)
        self.setts = setts
        self.settings = []
        self.web_sProc = {}
        self.mysql_sProc = {}

    log = pyqtSignal(list, arguments=['logger'])
    logDB = pyqtSignal(list, arguments=['logger'])
    sendStatusInfo = pyqtSignal(list, arguments=['sendStatus'])
    changedPort = pyqtSignal(str, arguments=['changed_port'])
    changedDBPort = pyqtSignal(str, arguments=['changed_db_port'])

    @pyqtSlot()
    def getStatus(self):

        ini_stat = threading.Thread(target=self.sendStatus)
        ini_stat.daemon = True
        ini_stat.start()

    def sendStatus(self):

        servers = setts._get_servers()
        self.sendStatusInfo.emit(servers)

    @pyqtSlot(int)
    def startServer(self, id):

        start_thread = threading.Thread(target=self._startServer, args=[id])
        start_thread.daemon = True
        start_thread.start()

    @pyqtSlot(int)
    def startDatabase(self, id):

        start_thread = threading.Thread(target=self._startDatabase, args=[id])
        start_thread.daemon = True
        start_thread.start()

    @pyqtSlot(int)
    def stopServer(self, id):

        stop_thread = threading.Thread(target=self._stopServer, args=[id])
        stop_thread.daemon = True
        stop_thread.start()

    @pyqtSlot(int)
    def stopDatabase(self, id):

        stop_thread = threading.Thread(target=self._stopDatabase, args=[id])
        stop_thread.daemon = True
        stop_thread.start()

    def _startServer(self, id):

        self._startWebServer(id)
        self._updateServerStatus(id, 'Running')
        self.logger(id, 'Running')

    def _startDatabase(self, id):
    
        self._startMySQL(id)
        self._updateDatabaseStatus(id, 'Running')
        self.db_logger(id, 'Running')

    def _stopServer(self, id):

        self._stopWebServer(id)
        self._updateServerStatus(id, 'Stopped')
        self.logger(id, 'Stopped')

    def _stopDatabase(self, id):
    
        self._stopMySQL(id)
        self._updateDatabaseStatus(id, 'Stopped')
        self.db_logger(id, 'Stopped')

    def _startWebServer(self, id):
        print(self.setts.servers[id]["path"])
        proc = subprocess.Popen([self.setts.servers[id]["path"],
                                           str(self.setts.servers[id]["port"])],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.STDOUT,
                                           shell=False)

        # store the pid
        pid = proc.pid
        self.web_sProc[id] = pid
        self.setts.save_server_pid(id, pid)

        return True

    def _stopWebServer(self, id):
        pid = self.web_sProc[id]
        p = psutil.Process(pid)
        p.terminate()

        # remove the pid
        self.web_sProc[id] = None
        self.setts.remove_server_pid(id)

        return True

    def _startMySQL(self, id):
        proc = subprocess.Popen(
                [self.setts.server[id]["path"]+"mysqld"],
                 stdout=subprocess.PIPE,
                 stderr=subprocess.STDOUT,
                 shell=False)

        # store the pid
        pid = proc.pid
        self.mysql_sProc[id] = pid
        self.setts.save_database_pid(id, pid)
        return True

    def _stopMySQL(self, id):
        pid = self.mysql_sProc[id]
        p = psutil.Process(pid)
        p.terminate()

        # remove the pid
        self.mysql_sProc[id] = None
        self.setts.remove_database_pid(id)
        return True

    def _updateServerStatus(self, index, new_sts):
        self.setts.servers[index]['status'] = new_sts

    def _updateDatabaseStatus(self, index, new_sts):
        self.setts.databases[index]['status'] = new_sts

    def logger(self, index, message):

        self.log.emit([index, message])

    def db_logger(self, index, message):
    
        self.logDB.emit([index, message])

    @pyqtSlot(str)
    def change_port(self, new_port):
        port_thread = threading.Thread(target=self._change_port,
                                       args=[new_port])
        port_thread.daemon = True
        port_thread.start()

    @pyqtSlot(str)
    def change_db_port(self, new_port):
        port_thread = threading.Thread(target=self._change_db_port,
                                       args=[new_port])
        port_thread.daemon = True
        port_thread.start()

    def _change_port(self, new_port):
        # changes the port
        self.setts.server[0]["port"] = int(new_port)
        # update UI code also
        self.changed_port(new_port)

    def _change_db_port(self, new_port):
        # changes the port
        self.setts.server[0]["port"] = int(new_port)
        # update UI code also
        self.changed_db_port(new_port)

    def changed_db_port(self, new_port):
        # send to Qml layer
        self.changedDBPort.emit(new_port)
