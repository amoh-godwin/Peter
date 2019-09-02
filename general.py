# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:17:28 2019

@author: Ampofo
"""
import threading
import subprocess
from PyQt5.QtCore import QObject, pyqtSlot

class GeneralFunc(QObject):


    def __init__(self):
        QObject.__init__(self)
        self.base_address = ""

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

    def _openApp(self):
        subprocess.run(["http://localhost:7773/"])

    def _openAppFolder(self):
        subprocess.run(["explorer", "C:\\Deuteronomy Works\\Peter\\Server"])

    def _openPhpMyAdmin(self):
        subprocess.run(["http://localhost:7773/phpmyadmin"])

    def _openSupport(self):
        subprocess.run(["http://deuteronomy-works.github.io/support"])