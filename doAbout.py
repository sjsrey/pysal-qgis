# -*- coding: utf-8 -*-
# licensed under the terms of GNU GPL 2
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
import webbrowser, os
from ui_frmAbout import Ui_Dialog
import resources
currentPath = os.path.dirname(__file__)

class Dialog(QDialog, Ui_Dialog):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		# Set up the user interface from Designer.
		self.setupUi(self)
		QObject.connect(self.btnWeb, SIGNAL("clicked()"), self.openWeb)
		QObject.connect(self.btnHelp, SIGNAL("clicked()"), self.openHelp)
		self.fToolsLogo.setPixmap(QPixmap(":/icons/default/about_logo.png"))
		self.label_3.setText("PySAL for QGIS 0.1")
		self.textEdit.setText(self.getText())

	def getText(self):
		return self.tr("""

This is a group project for GPH 498/598 Geocomputation.

The goal is to create a plug-in for QGIS (AKA Quantum GIS) that enables a subset of PySAL functionality.

Collaborators
sjsrey
madhavg
gelasher
kkane5
evazhang417
""")

	def openWeb(self):
		webbrowser.open("http://code.google.com/p/pysal/")

	def openHelp(self):
		webbrowser.open("http://pysal.geodacenter.org/1.4/users/index.html")
