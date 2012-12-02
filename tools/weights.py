
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ftools_utils
from qgis.core import *
from ui_weights import Ui_Weight

import pysal as PS
import numpy as NP

class weightsdialog(QDialog, Ui_Weight):

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface
        # Set up the user interface from Designer.
        self.setupUi(self)
        # QObject.connect(self.toolOut, SIGNAL("clicked()"), self.outFile)
	QObject.connect(self.comboBox, SIGNAL("clicked()"), self.contiguity_from_shapefile(inPoly, criteria == 'rook'))
        self.setWindowTitle(self.tr("Weights from Shapefile"))
        self.generateWeights = self.pushButton( QPushButton.Ok )
        # populate layer list
        # self.progressBar.setValue(0)
        mapCanvas = self.iface.mapCanvas()
        # layers = ftools_utils.getLayerNames([QGis.Line])
        # self.inPoint.addItems(layers)
        layers = ftools_utils.getLayerNames([QGis.Polygon])
        self.comboBox.addItems(layers)
    
    def accept(self):
        self.comboBox.setEnabled( False )
        if self.comboBox.currentText() == "":
            QMessageBox.information(self, self.tr("Generate weights from shapefile"), self.tr("Please specify input polygon vector layer"))
        # elif self.outShape.text() == "":
            # QMessageBox.information(self, self.tr("Sum Line Lengths In Polyons"), self.tr("Please specify output shapefile"))
        # elif self.inPoint.currentText() == "":
            # QMessageBox.information(self, self.tr("Sum Line Lengths In Polyons"), self.tr("Please specify input line vector layer"))
        # elif self.lnField.text() == "":
            # QMessageBox.information(self, self.tr("Sum Line Lengths In Polyons"), self.tr("Please specify output length field"))
        else:
            inPoly = self.comboBox.currentText()
            # inLns = self.inPoint.currentText()
            # inField = self.lnField.text()
            # outPath = self.outShape.text()
            # if outPath.contains("\\"):
            #    outName = outPath.right((outPath.length() - outPath.lastIndexOf("\\")) - 1)
            # else:
            #    outName = outPath.right((outPath.length() - outPath.lastIndexOf("/")) - 1)
            # if outName.endsWith(".shp"):
            #    outName = outName.left(outName.length() - 4)
            # self.compute(inPoly, inLns, inField, outPath, self.progressBar)
            # self.outShape.clear()
            # addToTOC = QMessageBox.question(self, self.tr("Sum line lengths"), self.tr("Created output shapefile:\n%1\n\nWould you like to add the new layer to the TOC?").arg(unicode(outPath)), QMessageBox.Yes, QMessageBox.No, QMessageBox.NoButton)
            #if addToTOC == QMessageBox.Yes:
            #    self.vlayer = QgsVectorLayer(outPath, unicode(outName), "ogr")
            #    QgsMapLayerRegistry.instance().addMapLayer(self.vlayer)
        # self.progressBar.setValue(0)
        self.pushButton.setEnabled( True )


    def contiguity_from_shapefile(shapefile, criteria='rook'):
        if criteria == 'rook':
	    PS.rook_from_shapefile(shapefile)
            abb = 'r'
    	else:
            PS.queen_from_shapefile(shapefile)
            abb = 'q'
    	    cards = NP.array(w.cardinalities.values())
    	    cards.shape = (len(cards),1)
    	    galfile = shapefile.split(".")[0] + "_" + abb + ".gal"
    	    gal = PS.open(galfile,'w')
    	    gal.write(w)
    	    gal.close()

    	return cards
