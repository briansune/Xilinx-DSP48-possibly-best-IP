# -*- coding: utf-8 -*-

import sys
import pyvisa as visa
import xdsp48_gui as _xdsp
import re
import threading
import time

try:
    from queue import Queue, Empty
except ImportError:
    from Queue import Queue, Empty  # python 2.x

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox
)
from PyQt5 import QtGui
from xdsp48_gui import Ui_oMainWind


class Window(QMainWindow, Ui_oMainWind):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.sys_ports = []
        self.ui = Ui_oMainWind()
        self.ui.setupUi(self)

        self.connectSignalsSlots()

    def closeEvent(self, event):
        if self.bConFlag:
            self.controlLinkUnlink()

    def connectSignalsSlots(self):
        self.regAtapReset()
        self.ui.oActAbout.triggered.connect(self.about)
        self.ui.oActExit.triggered.connect(self.closeAct)

    def regAtapReset(self):
        print("\r\nTab Reg A")
        for widget in self.ui.tabMainWin.widget(1).children():
            print(widget.objectName())

        print("\r\nTab Reg D")
        for widget in self.ui.tabMainWin.widget(2).children():
            print(widget.objectName())

        print("\r\nTab Reg B")
        for widget in self.ui.tabMainWin.widget(3).children():
            print(widget.objectName())

    def closeAct(self):
        if self.bConFlag:
            self.controlLinkUnlink()
        self.close()

    @staticmethod
    def about():
        o_msg_box = QMessageBox()
        o_msg_box.setWindowTitle("Xilinx DSP48 Tool")
        o_msg_box.setText("<p>Designer: Brfo</p>"
                          "<p>Contact: briansune@gmail.com</p>"
                          "<p>Date: 2022</p>")
        o_msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
