# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:17:28 2019

@author: Ampofo
"""
import threading
import subprocess
import os
from PyQt5.QtCore import QObject, pyqtSlot

class GeneralFunc(QObject):


    def __init__(self, setts):
        QObject.__init__(self)
        self.setts = setts

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
        
        subprocess.run(['explorer', self.setts.addr])

    def _openAppFolder(self):
        url = os.path.abspath(os.path.join(self.setts.parent_folder, "Server"))
        subprocess.run(["explorer", url])

    def _openPhpMyAdmin(self):
        url = self.addr + "phpmyadmin"
        subprocess.run(['explorer', url])

    def _openSupport(self):
        subprocess.run(['explorer', "http://deuteronomy-works.github.io/support"])

