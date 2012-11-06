# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_Pysal.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Pysal(object):
    def setupUi(self, Pysal):
        Pysal.setObjectName("Pysal")
        Pysal.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Pysal)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Pysal)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Pysal.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Pysal.reject)
        QtCore.QMetaObject.connectSlotsByName(Pysal)

    def retranslateUi(self, Pysal):
        Pysal.setWindowTitle(QtGui.QApplication.translate("Pysal", "Pysal", None, QtGui.QApplication.UnicodeUTF8))
