# build global moran's I method. this will produce a single I variable

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import qgis.utils
import ftools_utils

from qgis.core import *
from Ui_globalMoran import Ui_Dialog

import pysal as py
import numpy as np
import math


class globalMoranDialog(QDialog, Ui_Dialog):

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)
        self.setWindowTitle(self.tr("Global Moran's I"))
        QObject.connect(self.inShape, SIGNAL("currentIndexChanged(QString)"), self.update)
	self.cancel_close = self.buttonBox.button( QDialogButtonBox.Close )	
	self.buttonOK = self.buttonBox.button( QDialogButtonBox.Ok )


	# Layer List
	self.layerList= (self.getLayerName([QGis.Polygon]))
        self.layerpaths = (self.getLayerPath([QGis.Polygon]))
        paths = tuple(self.layerpaths)
        names = tuple(self.layerList)
        self.dic = dict(zip(names,paths))
        for layer in self.layerList:
            self.inShape.addItem(layer)
	
    # check for shapefiles and fields
    def accept(self):
	self.buttonOK.setEnabled( False )
	if self.inShape.currentText() == "":
            QMessageBox.information(self, self.tr("Global Moran's I"), self.tr("Please specify input shapefile"))
        elif self.inField.currentText() == "":
            QMessageBox.information(self, self.tr("GLobal Moran's I"), self.tr("Please specify target field"))
        elif self.idVariable.currentText() == "":
            QMessageBox.information(self, self.tr("Global Moran's I"), self.tr("Please specify Weight Matrix unique ID field"))
        else:
            if str(self.inShape.currentText()) == "":
               vlayer = str(self.layerpaths)
            else:
               vlayer = str(self.dic[str(self.inShape.currentText())])
            
	    tfield=self.inField.currentText()
	    idvar=self.idVariable.currentText()
	    if self.rook.isChecked():matType="Rook"
	    else: matType="Queen"
	    self.compute(vlayer,tfield,idvar,matType)
	    self.buttonOK.setEnabled( True )

    # designates the selected shapefile as the layer to pick attributes from
    def update(self,inputLayer):
	self.inField.clear()
	self.idVariable.clear()
	inputLayer=unicode(self.inShape.currentText())
	if inputLayer != "":
	    changedLayer=ftools_utils.getVectorLayerByName(inputLayer)
	    changedField=ftools_utils.getFieldList(changedLayer)
	    changedID=ftools_utils.getFieldList(changedLayer)
	    for i in changedField:	
                if changedField[i].typeName() != "String":
	           self.inField.addItem(unicode(changedField[i].name()))
	    for i in changedID:
	        if changedID[i].typeName() != "String":
	           self.idVariable.addItem(unicode(changedID[i].name()))
	

    # run the pysal logic for global moran's I
    def compute(self, vlayer, tfield, idvar,matType):
	vlayer=qgis.utils.iface.activeLayer()
	idvar=self.idVariable.currentText()
	tfield=self.inField.currentText()
	provider=vlayer.dataProvider()
	allAttrs=provider.attributeIndexes()
	caps=vlayer.dataProvider().capabilities()
	if caps & QgsVectorDataProvider.AddAttributes:
            TestField = idvar[:5]+"_qrr"
	    res = vlayer.dataProvider().addAttributes([QgsField(TestField, QVariant.Double)])
	wp=str(self.dic[str(self.inShape.currentText())])
        if matType == "Rook":
           w = py.rook_from_shapefile(wp, idVariable=unicode(idvar))
        else:
           w = py.queen_from_shapefile(wp, idVariable=unicode(idvar))

	w1=wp[:-3]+"dbf"
	db=py.open(w1)
	y=np.array(db.by_col[unicode(tfield)])
	mi = py.Moran(y,w)
	mg = mi.I
        self.SAresult.setText(str(mg))

    # read file path for pysal inputs from open shapefiles
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
            else:
                pass
        return layerPathList

    # read layer names for gui display
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
