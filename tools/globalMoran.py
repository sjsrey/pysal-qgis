
#---------------------------------------------------------------------

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ftools_utils
from qgis.core import *
from Ui_globalMoran import Ui_Dialog

class globalMoranDialog(QDialog, Ui_Dialog):

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)
        self.setWindowTitle(self.tr("Global Moran's I"))
            
