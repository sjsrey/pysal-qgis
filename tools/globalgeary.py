# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'globalgearyy.ui'
#
# Created: Thu Nov 29 18:40:40 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_globalgeary(object):
    def setupUi(self, globalgeary):
        globalgeary.setObjectName(_fromUtf8("globalgeary"))
        globalgeary.resize(578, 464)
        globalgeary.setWindowTitle(QtGui.QApplication.translate("globalgeary", "globalgeary", None, QtGui.QApplication.UnicodeUTF8))
        self.datsrc = QtGui.QLabel(globalgeary)
        self.datsrc.setGeometry(QtCore.QRect(30, 40, 121, 21))
        self.datsrc.setText(QtGui.QApplication.translate("globalgeary", "Select data source", None, QtGui.QApplication.UnicodeUTF8))
        self.datsrc.setObjectName(_fromUtf8("datsrc"))
        self.curlar = QtGui.QRadioButton(globalgeary)
        self.curlar.setGeometry(QtCore.QRect(180, 40, 131, 21))
        self.curlar.setText(QtGui.QApplication.translate("globalgeary", "Current Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.curlar.setObjectName(_fromUtf8("curlar"))
        self.newfil = QtGui.QRadioButton(globalgeary)
        self.newfil.setGeometry(QtCore.QRect(180, 70, 141, 21))
        self.newfil.setText(QtGui.QApplication.translate("globalgeary", "Select File Path", None, QtGui.QApplication.UnicodeUTF8))
        self.newfil.setObjectName(_fromUtf8("newfil"))
        self.newfilpath = QtGui.QComboBox(globalgeary)
        self.newfilpath.setGeometry(QtCore.QRect(330, 70, 211, 21))
        self.newfilpath.setObjectName(_fromUtf8("newfilpath"))
        self.Selatt = QtGui.QLabel(globalgeary)
        self.Selatt.setGeometry(QtCore.QRect(30, 140, 121, 21))
        self.Selatt.setText(QtGui.QApplication.translate("globalgeary", "Select attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.Selatt.setObjectName(_fromUtf8("Selatt"))
        self.selatt_dr = QtGui.QComboBox(globalgeary)
        self.selatt_dr.setGeometry(QtCore.QRect(180, 140, 211, 21))
        self.selatt_dr.setObjectName(_fromUtf8("selatt_dr"))
        self.selwei = QtGui.QLabel(globalgeary)
        self.selwei.setGeometry(QtCore.QRect(30, 200, 121, 21))
        self.selwei.setText(QtGui.QApplication.translate("globalgeary", "Select weights", None, QtGui.QApplication.UnicodeUTF8))
        self.selwei.setObjectName(_fromUtf8("selwei"))
        self.radioButton = QtGui.QRadioButton(globalgeary)
        self.radioButton.setGeometry(QtCore.QRect(180, 200, 161, 21))
        self.radioButton.setText(QtGui.QApplication.translate("globalgeary", "Threshold Distance", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(globalgeary)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 230, 241, 21))
        self.radioButton_2.setText(QtGui.QApplication.translate("globalgeary", "Adjacent Polygons (Queen) order", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(globalgeary)
        self.radioButton_3.setGeometry(QtCore.QRect(180, 290, 161, 21))
        self.radioButton_3.setText(QtGui.QApplication.translate("globalgeary", "K Nearest Neighbors", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(globalgeary)
        self.radioButton_4.setGeometry(QtCore.QRect(180, 260, 221, 16))
        self.radioButton_4.setText(QtGui.QApplication.translate("globalgeary", "Shared Boundaries (Rook) order", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.K = QtGui.QLabel(globalgeary)
        self.K.setGeometry(QtCore.QRect(380, 290, 31, 16))
        self.K.setText(QtGui.QApplication.translate("globalgeary", "K =", None, QtGui.QApplication.UnicodeUTF8))
        self.K.setObjectName(_fromUtf8("K"))
        self.lineEdit = QtGui.QLineEdit(globalgeary)
        self.lineEdit.setGeometry(QtCore.QRect(420, 200, 113, 23))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(globalgeary)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 230, 113, 23))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(globalgeary)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 290, 113, 23))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(globalgeary)
        self.lineEdit_4.setGeometry(QtCore.QRect(420, 260, 113, 23))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.radioButton_9 = QtGui.QRadioButton(globalgeary)
        self.radioButton_9.setGeometry(QtCore.QRect(320, 380, 61, 21))
        self.radioButton_9.setText(QtGui.QApplication.translate("globalgeary", "9999", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_9.setObjectName(_fromUtf8("radioButton_9"))
        self.radioButton_10 = QtGui.QRadioButton(globalgeary)
        self.radioButton_10.setGeometry(QtCore.QRect(250, 380, 61, 21))
        self.radioButton_10.setText(QtGui.QApplication.translate("globalgeary", "999", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_10.setObjectName(_fromUtf8("radioButton_10"))
        self.radioButton_11 = QtGui.QRadioButton(globalgeary)
        self.radioButton_11.setGeometry(QtCore.QRect(170, 380, 61, 21))
        self.radioButton_11.setText(QtGui.QApplication.translate("globalgeary", "99", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_11.setObjectName(_fromUtf8("radioButton_11"))
        self.lineEdit_6 = QtGui.QLineEdit(globalgeary)
        self.lineEdit_6.setGeometry(QtCore.QRect(480, 380, 41, 21))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.radioButton_12 = QtGui.QRadioButton(globalgeary)
        self.radioButton_12.setGeometry(QtCore.QRect(400, 380, 61, 21))
        self.radioButton_12.setText(QtGui.QApplication.translate("globalgeary", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_12.setObjectName(_fromUtf8("radioButton_12"))
        self.perm = QtGui.QLabel(globalgeary)
        self.perm.setGeometry(QtCore.QRect(30, 360, 201, 16))
        self.perm.setText(QtGui.QApplication.translate("globalgeary", "Number of Random Permutations", None, QtGui.QApplication.UnicodeUTF8))
        self.perm.setObjectName(_fromUtf8("perm"))
        self.buttonBox = QtGui.QDialogButtonBox(globalgeary)
        self.buttonBox.setGeometry(QtCore.QRect(410, 430, 156, 25))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(globalgeary)
        QtCore.QMetaObject.connectSlotsByName(globalgeary)

    def retranslateUi(self, globalgeary):
        pass

