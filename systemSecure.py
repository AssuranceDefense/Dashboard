# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/nraikman2022/PycharmProjects/ProtechGunDefense/systemSecure.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import requests
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(746, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gunDetected = QtWidgets.QLabel(self.centralwidget)
        self.gunDetected.setGeometry(QtCore.QRect(180, 10, 371, 41))
        self.gunDetected.setObjectName("gunDetected")
        self.gunIsDetected = QtWidgets.QLabel(self.centralwidget)
        self.gunIsDetected.setGeometry(QtCore.QRect(270, 100, 211, 171))
        self.gunIsDetected.setObjectName("gunIsDetected")
        self.gunIsNotDetected = QtWidgets.QLabel(self.centralwidget)
        self.gunIsNotDetected.setGeometry(QtCore.QRect(270, 100, 211, 201))
        self.gunIsNotDetected.setObjectName("gunIsNotDetected")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 746, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QtWidgets.QApplication.processEvents()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.show()
        QtWidgets.QApplication.processEvents()
        d = requests.get("http://34.201.116.202/checkStatus")
        if d.text == "True":
            self.gunIsNotDetected.hide()
            self.gunIsDetected.show()
        else:
            self.gunIsDetected.hide()
            self.gunIsNotDetected.show()

        QtWidgets.QApplication.processEvents()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gunDetected.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">System Security Status</span></p><p><br/></p></body></html>"))
        self.gunIsDetected.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/gunIsDetected/x.png\" width=\"200\"></p></body></html>"))
        self.gunIsNotDetected.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/gunIsNotDetected/checkmark.png\" width=\"200\"/></p></body></html>"))
        self.timer = QtCore.QTimer.singleShot(0, self.retranslateUi(MainWindow))

import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
