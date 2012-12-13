# Plugin for creating a .gal file from vector Polygons.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ftools_utils
from PyQt4 import QtCore, QtGui
from qgis.core import *
from ui_weights import Ui_Dialog

import pysal as PS
import numpy as NP

class weightsdialog(QDialog, Ui_Dialog):

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface
        # Set up the user interface from Designer.
        self.setupUi(self)
        # define global shapefile variable
        self.shapefile = ''
        QObject.connect(self.toolButton, SIGNAL("clicked()"), self.namefile)
        self.setWindowTitle(self.tr("Generate Weights"))

        mapCanvas = self.iface.mapCanvas()
        # When there is no layer picked for the browse box, will initialize
        # the global variable to be an empty string
        self.lineEdit.setText("")

        self.shapefile = (self.getLayerPath([QGis.Polygon]))
        self.shapefileNames = (self.getLayerName([QGis.Polygon]))
        paths = tuple(self.shapefile)
        names = tuple(self.shapefileNames)
        self.d = dict(zip(names,paths))

        # insert paths into combo box
        for layer in self.shapefileNames:
            self.comboBox.addItem(layer)
    
    # Define method to run the plugin (includes PySAL logic)
    def accept(self):
        # look for open shapefile layers, if none 
        if len(self.comboBox.currentText()) == 0 and self.lineEdit.text() == "":
            QMessageBox.information(self, self.tr("Weights from Shapefile"), self.tr("Please select input polygon vector layer"))

        # elif self.outShape.text() == "":
        #    QMessageBox.information(self, self.tr("Sum Line Lengths In Polyons"), self.tr("Please specify output shapefile"))
        else:
            # run the PySAL logic
            if str(self.comboBox.currentText()) == "":
                shapefile = str(self.shapefile)
            else:
                shapefile = str(self.d[str(self.comboBox.currentText())])
                       
                if self.radioButton.isChecked():
                    w = PS.queen_from_shapefile(shapefile)
                    abb = 'q'
                else:
                    w = PS.rook_from_shapefile(shapefile)
                    abb = 'r'
    	        cards = NP.array(w.cardinalities.values())
    	        cards.shape = (len(cards),1)
    	        galfile = shapefile.split(".")[0] + "_" + abb + ".gal"
    	        gal = PS.open(galfile,'w')
    	        gal.write(w)
    	        gal.close()
            QDialog.accept(self)

    # Browse file method
    def namefile(self):
        self.shapefile = QFileDialog.getOpenFileName(self, 'Open shape', '/home', 'Shape Files (*.shp)')
        self.lineEdit.setText(str(self.shapefile))
        print self.shapefile
        

    #def outFile(self):
    #    self.outShape.clear()
    #    ( self.shapefileName, self.encoding ) = ftools_utils.saveDialog( self )
    #    if self.shapefileName is None or self.encoding is None:
    #        return
    #    self.outShape.setText( QString( self.shapefileName ) )

    # Define method for building file paths for PySAL from open layers in QGIS
    def getLayerPath( self, vTypes ):
        layermap = QgsMapLayerRegistry.instance().mapLayers()
        layerPathList = []
        for name, layer in layermap.iteritems():
            if layer.type() == QgsMapLayer.VectorLayer:
                if layer.geometryType() in vTypes:
                    fullPath = unicode( layer.dataProvider().dataSourceUri() )
                    fullPath = fullPath.split('|')[0]
                    fullPath = fullPath.split("u'")[-1]
                    layerPathList.append(str(fullPath))
                    # print layerlist
            else:
                pass
        return layerPathList

    def getLayerName( self, vTypes ):
        layermap = QgsMapLayerRegistry.instance().mapLayers()
        layerNameList = []
        for name, layer in layermap.iteritems():
            if layer.type() == QgsMapLayer.VectorLayer:
                if layer.geometryType() in vTypes:
                    layerNameList.append( unicode( layer.name() ) )
            else:
                pass
        return layerNameList

