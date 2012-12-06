# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'globalMoran.ui'
#
# Created: Thu Dec  6 12:20:21 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(401, 416)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 380, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 364, 52))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.VLayout1 = QtGui.QVBoxLayout(self.layoutWidget)
        self.VLayout1.setMargin(0)
        self.VLayout1.setObjectName(_fromUtf8("VLayout1"))
        self.label1 = QtGui.QLabel(self.layoutWidget)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.VLayout1.addWidget(self.label1)
        self.inShape = QtGui.QComboBox(self.layoutWidget)
        self.inShape.setObjectName(_fromUtf8("inShape"))
        self.VLayout1.addWidget(self.inShape)
        self.layoutWidget_2 = QtGui.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 70, 361, 52))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.VLayout2 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.VLayout2.setMargin(0)
        self.VLayout2.setObjectName(_fromUtf8("VLayout2"))
        self.label2 = QtGui.QLabel(self.layoutWidget_2)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.VLayout2.addWidget(self.label2)
        self.inField = QtGui.QComboBox(self.layoutWidget_2)
        self.inField.setObjectName(_fromUtf8("inField"))
        self.VLayout2.addWidget(self.inField)
        self.layoutWidget_3 = QtGui.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 130, 361, 52))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.VLayout3 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.VLayout3.setMargin(0)
        self.VLayout3.setObjectName(_fromUtf8("VLayout3"))
        self.label3 = QtGui.QLabel(self.layoutWidget_3)
        self.label3.setObjectName(_fromUtf8("label3"))
        self.VLayout3.addWidget(self.label3)
        self.inWeight = QtGui.QComboBox(self.layoutWidget_3)
        self.inWeight.setObjectName(_fromUtf8("inWeight"))
        self.VLayout3.addWidget(self.inWeight)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 200, 361, 171))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.VLayout4 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.VLayout4.setMargin(0)
        self.VLayout4.setObjectName(_fromUtf8("VLayout4"))
        self.label4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label4.setObjectName(_fromUtf8("label4"))
        self.VLayout4.addWidget(self.label4)
        self.textBrowser = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.VLayout4.addWidget(self.textBrowser)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("Dialog", "Input Shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("Dialog", "Target field", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setText(QtGui.QApplication.translate("Dialog", "Weights Matrix FIle", None, QtGui.QApplication.UnicodeUTF8))
        self.label4.setText(QtGui.QApplication.translate("Dialog", "Spatial Autocorrelation Result", None, QtGui.QApplication.UnicodeUTF8))

