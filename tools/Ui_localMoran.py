# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'localMoran.ui'
#
# Created: Thu Dec 13 05:59:20 2012
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
        Dialog.resize(391, 428)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 390, 271, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 361, 52))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.VLayout_1 = QtGui.QVBoxLayout(self.layoutWidget)
        self.VLayout_1.setMargin(0)
        self.VLayout_1.setObjectName(_fromUtf8("VLayout_1"))
        self.label1 = QtGui.QLabel(self.layoutWidget)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.VLayout_1.addWidget(self.label1)
        self.inShape = QtGui.QComboBox(self.layoutWidget)
        self.inShape.setObjectName(_fromUtf8("inShape"))
        self.VLayout_1.addWidget(self.inShape)
        self.layoutWidget_2 = QtGui.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 70, 361, 52))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.VLayout_2 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.VLayout_2.setMargin(0)
        self.VLayout_2.setObjectName(_fromUtf8("VLayout_2"))
        self.label2 = QtGui.QLabel(self.layoutWidget_2)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.VLayout_2.addWidget(self.label2)
        self.inField = QtGui.QComboBox(self.layoutWidget_2)
        self.inField.setObjectName(_fromUtf8("inField"))
        self.VLayout_2.addWidget(self.inField)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 270, 361, 103))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.VLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.VLayout_5.setMargin(0)
        self.VLayout_5.setObjectName(_fromUtf8("VLayout_5"))
        self.label5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label5.setObjectName(_fromUtf8("label5"))
        self.VLayout_5.addWidget(self.label5)
        self.SAresult = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.SAresult.setEnabled(True)
        self.SAresult.setObjectName(_fromUtf8("SAresult"))
        self.VLayout_5.addWidget(self.SAresult)
        self.layoutWidget_4 = QtGui.QWidget(Dialog)
        self.layoutWidget_4.setGeometry(QtCore.QRect(20, 130, 361, 52))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.VLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.VLayout_3.setMargin(0)
        self.VLayout_3.setObjectName(_fromUtf8("VLayout_3"))
        self.label3 = QtGui.QLabel(self.layoutWidget_4)
        self.label3.setObjectName(_fromUtf8("label3"))
        self.VLayout_3.addWidget(self.label3)
        self.idVariable = QtGui.QComboBox(self.layoutWidget_4)
        self.idVariable.setObjectName(_fromUtf8("idVariable"))
        self.VLayout_3.addWidget(self.idVariable)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 190, 361, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.queen = QtGui.QRadioButton(self.groupBox)
        self.queen.setGeometry(QtCore.QRect(0, 20, 359, 22))
        self.queen.setObjectName(_fromUtf8("queen"))
        self.rook = QtGui.QRadioButton(self.groupBox)
        self.rook.setGeometry(QtCore.QRect(0, 40, 359, 22))
        self.rook.setObjectName(_fromUtf8("rook"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 390, 171, 27))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("Dialog", "Input Shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("Dialog", "Target field", None, QtGui.QApplication.UnicodeUTF8))
        self.label5.setText(QtGui.QApplication.translate("Dialog", "Spatial Autocorrelation Result", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setText(QtGui.QApplication.translate("Dialog", "Weights FIle ID Variable", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Contiguity Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.queen.setText(QtGui.QApplication.translate("Dialog", "Queen Contiguity", None, QtGui.QApplication.UnicodeUTF8))
        self.rook.setText(QtGui.QApplication.translate("Dialog", "Rook Contiguity", None, QtGui.QApplication.UnicodeUTF8))

