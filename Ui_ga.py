# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_ga.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ga(object):
    def setupUi(self, ga):
        ga.setObjectName("ga")
        ga.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(ga)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(ga)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ga.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ga.reject)
        QtCore.QMetaObject.connectSlotsByName(ga)

    def retranslateUi(self, ga):
        ga.setWindowTitle(QtGui.QApplication.translate("ga", "ga", None, QtGui.QApplication.UnicodeUTF8))
