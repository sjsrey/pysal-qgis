# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_lisa4qgis.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_lisa4qgis(object):
    def setupUi(self, lisa4qgis):
        lisa4qgis.setObjectName("lisa4qgis")
        lisa4qgis.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(lisa4qgis)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(lisa4qgis)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), lisa4qgis.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), lisa4qgis.reject)
        QtCore.QMetaObject.connectSlotsByName(lisa4qgis)

    def retranslateUi(self, lisa4qgis):
        lisa4qgis.setWindowTitle(QtGui.QApplication.translate("lisa4qgis", "lisa4qgis", None, QtGui.QApplication.UnicodeUTF8))
