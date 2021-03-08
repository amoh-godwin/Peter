import threading
import subprocess
import os
import socket

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
    changedPort = pyqtSignal(int, str, arguments=['changed_port'])
    changedDBPort = pyqtSignal(int, str, arguments=['changed_db_port'])
    rejectPortChange = pyqtSignal(str, arguments=['_change_port', '_change_db_port'])

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
        # pid = self.web_sProc[id]
        pid = self.setts.get_server_pid(id)

        try:
            p = psutil.Process(int(pid))
            p.terminate()
        except:
            # psutil.NoSuchProcess
            # probably
            pass

        # remove the pid
        self.web_sProc[id] = None
        self.setts.remove_server_pid(id)

        return True

    def _startMySQL(self, id):
        path = os.path.join(self.setts.databases[id]["path"], "bin", "mysqld")
        proc = subprocess.Popen(
                [path],
                 stdout=subprocess.PIPE,
                 stderr=subprocess.STDOUT,
                 shell=False)

        # store the pid
        pid = proc.pid
        self.mysql_sProc[id] = pid
        self.setts.save_database_pid(id, pid)
        return True

    def _stopMySQL(self, id):
        # pid = self.mysql_sProc[id]
        pid = self.setts.get_database_pid(id)
        
        try:
            p = psutil.Process(int(pid))
            p.terminate()
        except:
            # psutil.NoSuchProcess
            # probably
            pass

        # remove the pid
        self.mysql_sProc[id] = None
        self.setts.remove_database_pid(id)
        return True

    def _updateServerStatus(self, index, new_sts):
        self.setts.servers[index]['status'] = new_sts
        self.setts._save_server_status(index, new_sts)

    def _updateDatabaseStatus(self, index, new_sts):
        self.setts.databases[index]['status'] = new_sts
        self.setts._save_database_status(index, new_sts)

    def logger(self, index, message):
        self.log.emit([index, message])

    def db_logger(self, index, message):
    
        self.logDB.emit([index, message])

    @pyqtSlot(int, str)
    def change_port(self, id, new_port):
        port_thread = threading.Thread(target=self._change_port,
                                       args=[id, new_port])
        port_thread.daemon = True
        port_thread.start()

    @pyqtSlot(int, str)
    def change_db_port(self, id, new_port):
        port_thread = threading.Thread(target=self._change_db_port,
                                       args=[id, new_port])
        port_thread.daemon = True
        port_thread.start()

    def _change_port(self, id, new_port):
        if self.check_port(int(new_port)):
            # changes the port
            self.setts.servers[id]["port"] = int(new_port)
            self.setts.change_server_port(id, int(new_port))
            # update UI code also
            self.changed_port(id, new_port)
        else:
            # reject the change
            msg = "Port is already in Use. Use another one"
            self.rejectPortChange.emit(msg)

    def _change_db_port(self, id, new_port):
        if self.check_port(int(new_port)):
            # changes the port
            self.setts.servers[id]["port"] = int(new_port)
            self.setts.change_database_port(id, int(new_port))
            # update UI code also
            self.changed_db_port(id, new_port)
        else:
            # reject the change
            msg = "Port is already in Use. Use another one"
            self.rejectPortChange.emit(msg)

    def changed_port(self, id, new_port):
        # send to Qml layer
        self.changedPort.emit(id, new_port)

    def changed_db_port(self, id, new_port):
        # send to Qml layer
        self.changedDBPort.emit(id, new_port)

    def check_port(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # in use
            s.connect(('127.0.0.1', port))
            return False
        except:
            return True
