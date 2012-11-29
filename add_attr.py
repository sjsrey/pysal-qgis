# Adding an attribute
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
layer = qgis.utils.iface.activeLayer()
provider = layer.dataProvider()
feat = QgsFeature()
caps = layer.dataProvider().capabilities()
if caps & QgsVectorDataProvider.AddAttributes:
	res = layer.dataProvider().addAttributes([QgsField("myint",QVariant.Int)])
# Changing Attribute Values
if caps & QgsVectorDataProvider.ChangeAttributeValues:
  attrs = { 0 : QVariant("hello"), 1 : QVariant(123) }
  layer.dataProvider().changeAttributeValues({ fid : attrs })

# try a QVariant of float ... for I's and p-values
# figure out update
