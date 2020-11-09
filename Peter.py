# -*- coding: utf-8 -*-
"""
@author: Amoh - Gyebi Godwin
# To You oh, LORD i commit myself
"""
import sys
import os
from PyQt5.QtCore import QCoreApplication, QResource
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from settings import Sets
from func import Switcher
from general import GeneralFunc
QResource.registerResource('peter.rcc')
def cleanUp():
    setts.save_file()

os.environ["QT_QUICK_CONTROLS_STYLE"] = "Universal"
app = QGuiApplication(sys.argv)
app.setWindowIcon(QIcon(":/UI/images/Peter.png"))
setts = Sets()
gen_func = GeneralFunc()
switcher = Switcher()

engine = QQmlApplicationEngine()

engine.load("./UI/qml/main.qml")

engine.rootObjects()[0].setProperty("general", gen_func)
engine.rootObjects()[0].setProperty("switcher", switcher)
engine.rootObjects()[0].setProperty("serversData", setts._get_servers())

engine.quit.connect(app.quit)
app.aboutToQuit.connect(cleanUp)
sys.exit(app.exec_())
 
