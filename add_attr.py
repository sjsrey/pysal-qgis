# Adding an attribute
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
layer = qgis.utils.iface.activeLayer()
provider = layer.dataProvider()
feat = QgsFeature()
caps = layer.dataProvider().capabilities()
if caps & QgsVectorDataProvider.AddAttributes:
 res = layer.dataProvider().addAttributes([QgsField("LISA",QVariant.Int)])

# This will come from pysal - placeholder for now
cluster = range(layer.featureCount())
for i in cluster:
 cluster[i] = cluster[i]*1.5

# This is the part that does all the work
a = range(layer.featureCount())
d = dict(zip(a,cluster)
n = len(allAtt) - 1
allAtt = provider.attributeIndexes()
for i in a:
 fid = i
 if caps & QgsVectorDataProvider.ChangeAttributeValues:
  attrs = { n : QVariant(d[i])}
  layer.dataProvider().changeAttributeValues({ fid : attrs })
layer.commitChanges()

