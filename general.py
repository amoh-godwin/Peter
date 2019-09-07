# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:17:28 2019

@author: Ampofo
"""
import threading
import subprocess
import os
import base64
import json
from PyQt5.QtCore import QObject, pyqtSlot

class GeneralFunc(QObject):


    def __init__(self):
        QObject.__init__(self)
        self.base_address = ""
        self.status_file = \
        "3ddb429e2f446edae3406bb9d0799eed7bddda600d9a05fe01d3baaa.settings"
        self.settings = None
        self.parent_folder = ""
        self.port = None
        self.addr = ""
        self.read_file()

    @pyqtSlot()
    def openApp(self):
        app_thread = threading.Thread(target=self._openApp)
        app_thread.daemon = True
        app_thread.start()

    @pyqtSlot()
    def openAppFolder(self):
        appf_thread = threading.Thread(target=self._openAppFolder)
        appf_thread.daemon = True
        appf_thread.start()

    @pyqtSlot()
    def openPhpMyAdmin(self):
        php_thread = threading.Thread(target=self._openPhpMyAdmin)
        php_thread.daemon = True
        php_thread.start()

    @pyqtSlot()
    def openSupport(self):
        sup_thread = threading.Thread(target=self._openSupport)
        sup_thread.daemon = True
        sup_thread.start()

    def read_file(self):

        with open(self.status_file, mode="rb") as sets_file:
            data = self._decrypt(sets_file.read())
            self.settings = json.loads(data)

        self.parent_folder = self.settings[0]["parent_folder"]
        server = self.settings[1]
        self.port = server[0]["port"]
        if self.port == 80:
            self.addr = "http://localhost/"
        else:
            self.addr = "http://localhost:" + str(self.port) + "/"

    def _encrypt(self, data):
        return base64.b64encode(bytes(str(data), 'ascii'))

    def _decrypt(self, data):
        decoded_data = base64.b64decode(data)
        str_data =  str(decoded_data, 'ascii')
        return str_data.replace("'", '"')

    def _openApp(self):
        
        subprocess.run(['explorer', self.addr])

    def _openAppFolder(self):
        url = os.path.abspath(os.path.join(self.parent_folder, "Server")) 
        print("url", url)
        subprocess.run(["explorer", url])

    def _openPhpMyAdmin(self):
        url = self.addr + "phpmyadmin"
        subprocess.run(['explorer', url])

    def _openSupport(self):
        subprocess.run(['explorer', "http://deuteronomy-works.github.io/support"])

