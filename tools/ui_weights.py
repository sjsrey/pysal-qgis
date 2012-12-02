# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weights.ui'
#
# Created: Sat Dec 01 16:32:14 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Weight(object):
    def setupUi(self, Weight):
        Weight.setObjectName(_fromUtf8("Weight"))
        Weight.resize(347, 175)
        Weight.setWindowTitle(QtGui.QApplication.translate("Weight", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.label = QtGui.QLabel(Weight)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setText(QtGui.QApplication.translate("Weight", "Shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(Weight)
        self.comboBox.setGeometry(QtCore.QRect(80, 20, 211, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.groupBox = QtGui.QGroupBox(Weight)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 281, 51))
        self.groupBox.setTitle(QtGui.QApplication.translate("Weight", "Contiguity", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton.setText(QtGui.QApplication.translate("Weight", "Rook", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 20, 82, 17))
        self.radioButton_2.setText(QtGui.QApplication.translate("Weight", "Queen", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.pushButton = QtGui.QPushButton(Weight)
        self.pushButton.setGeometry(QtCore.QRect(20, 140, 141, 21))
        self.pushButton.setText(QtGui.QApplication.translate("Weight", "Generate Weghts Object", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Weight)
        self.pushButton_2.setGeometry(QtCore.QRect(224, 140, 91, 21))
        self.pushButton_2.setText(QtGui.QApplication.translate("Weight", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Weight)
        QtCore.QMetaObject.connectSlotsByName(Weight)

    def retranslateUi(self, Weight):
        pass

