import os
import sys


import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import sqlite3
from PyQt5 import QtWidgets


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('screen1.ui', self)
        self.button.clicked.connect(self.pb)

    def pb(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        loadUi('screen2.ui', self)
        self.label = self.label
        self.button2.clicked.connect(self.pb2)

    def pb2(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

        
    
    
# main
app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow = MainWindow()
screen2 = Screen2()
widget.addWidget(mainwindow)
widget.addWidget(screen2)
widget.setFixedHeight(300)
widget.setFixedWidth(400)
widget.show()

try:
    sys.exit(app.exec())
except:
    print('exiting')




