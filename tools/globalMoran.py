
#---------------------------------------------------------------------

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
	mapCanvas=self.iface.mapCanvas()
	layerList= ftools_utils.getLayerNames([QGis.Polygon])
	self.inShape.addItems(layerList)
	
    def accept(self):
	self.buttonOK.setEnabled( False )
	if self.inShape.currentText() == "":
            QMessageBox.information(self, self.tr("Global Moran's I"), self.tr("Please specify input shapefile"))
        elif self.inField.currentText() == "":
            QMessageBox.information(self, self.tr("Global Moran's I"), self.tr("Please specify target field"))
        elif self.idVariable.currentText() == "":
            QMessageBox.information(self, self.tr("Global Moran's I"), self.tr("Please specify Weight Matrix unique ID field"))
        else:
	    vlayer=self.inShape.currentText()
	    tfield=self.inField.currentText()
	    idvar=self.idVariable.currentText()
	    if self.rook.isChecked():matType="Rook"
	    else: matType="Queen"
	    self.compute(vlayer,tfield,idvar)
	    self.buttonOK.setEnabled( True )


    def update(self,inputLayer):
	self.inField.clear()
	self.idVariable.clear()
	inputLayer=unicode(self.inShape.currentText())
	if inputLayer != "":
	    changedLayer=ftools_utils.getVectorLayerByName(inputLayer)
	    changedField=ftools_utils.getFieldList(changedLayer)
	    changedID=ftools_utils.getFieldList(changedLayer)
	    for i in changedField:	
	        #if changedField[i].type() == QVariant.Int or \
		#changedField[i].type() == QVariant.String:
	        self.inField.addItem(unicode(changedField[i].name()))
	    for i in changedID:
	        #if changedID[i].type() == QVariant.Int or \
	        #changedID[i].type() == QVariant.String:
	        self.idVariable.addItem(unicode(changedID[i].name()))
	


    #def rookMatrix(self, provider1, provider2, index1, index2)       
    def compute(self, vlayer, tfield, idvar):
	vlayer=qgis.utils.iface.activeLayer()
	idvar=self.idVariable.currentText()
        print type(idvar)
	tfield=self.inField.currentText()
        print type(tfield)
	provider=vlayer.dataProvider()
	allAttrs=provider.attributeIndexes()
	caps=vlayer.dataProvider().capabilities()
	if caps & QgsVectorDataProvider.AddAttributes:
	    res = vlayer.dataProvider().addAttributes([QgsField("TestField", QVariant.Double)])
	wp="/home/evazhang/pysal-qgis/dev/Iowa.shp"
	w=py.rook_from_shapefile(wp, idVariable=unicode(idvar))
	w1=wp[:-3]+"dbf"
	db=py.open(w1)
	y=np.array(db.by_col[unicode(tfield)])
      	np.random.seed(12345)
	lm=py.Moran_Local(y,w)
	l=lm.p_sim
	
	# Replace insignificant values with the number 5:
	for i in range(len(l)):
	    if l[i] > 0.05:
		l[i] = 5 

	# Replace the significant values with their quadrant:
	for i in range(len(l)):
	    if l[i] <= 0.05:
		l[i] =lm.q[i] 

	a=range(len(l))
	l1=np.array(l).flatten().tolist()
	d=dict(zip(a,l1))
	fieldList=ftools_utils.getFieldList(vlayer)
	print len(fieldList)
	n=len(fieldList)-1
	vlayer.startEditing()
	for i in a:
	    fid=int(i)
	    print fid
	    vlayer.changeAttributeValue(fid,n,d[i])
	    print d[i] #index of the new added field
	vlayer.commitChanges()
	#if vlayer.commitChanges() == "True": self.SAresult.text()="Done!"
	#else: self.SAresult.text()="Can't make it!"
  

	

