# build the about dialog

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

This plug-in for QGIS (AKA Quantum GIS) enables a subset of PySAL functionality.

Collaborators:
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
