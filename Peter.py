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
from func import Switcher

os.environ["QT_QUICK_CONTROLS_STYLE"] = "Universal"
# QResource.registerResource("")
app = QGuiApplication(sys.argv)
# app.setWindowIcon(QIcon(""))
switcher = Switcher()

engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty("Switcher", switcher)
engine.load("UI/qml/main.qml")
engine.quit.connect(app.quit)
sys.exit(app.exec_())
