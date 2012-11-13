# 1. Iterating over Vector Layer
# Below is an example how to go through the features of the layer.
# To read features from layer, initialize the retieval with select() and then use nextFeature() calls

provider = vlayer.dataProvider()

feat = QgsFeature()
allAttrs = provider.attributeIndexes()

# start data retreival: fetch geometry and all attributes for each feature
provider.select(allAttrs)

# retreive every feature with its geometry and attributes
while provider.nextFeature(feat):

  # fetch geometry
  geom = feat.geometry()
  print "Feature ID %d: " % feat.id() ,

  # show some information about the feature
  if geom.vectorType() == QGis.Point:
    x = geom.asPoint()
    print "Point: " + str(x)
  elif geom.vectorType() == QGis.Line:
    x = geom.asPolyline()
    print "Line: %d points" % len(x)
  elif geom.vectorType() == QGis.Polygon:
    x = geom.asPolygon()
    numPts = 0
    for ring in x:
      numPts += len(ring)
    print "Polygon: %d rings with %d points" % (len(x), numPts)
  else:
    print "Unknown"

  # fetch map of attributes
  attrs = feat.attributeMap()

  # attrs is a dictionary: key = field index, value = QgsFeatureAttribute
  # show all attributes and their values
  for (k,attr) in attrs.iteritems():
    print "%d: %s" % (k, attr.toString())

"""

1. fetchAttributes: List of attributes which should be fetched. 
   Default: empty list

2. rect: Spatial filter. 
   If empty rect is given (QgsRectangle()), all features are fetched.
   Default: empty rect

3. fetchGeometry:Whether geometry of the feature should be fetched. 
   Default: True

4. useIntersect: When using spatial filter, this argument says whether accurate test for intersection should be done or whether test on bounding box suffices.This is needed e.g. for feature identification or selection. 
   Default: False

"""

# 2. to obtain field index from its name
fldDesc = provider.fieldNameIndex("DESCRIPTION")
if fldDesc == -1:
  print "Field not found!"

# 3. adding and removing fields
if caps & QgsVectorDataProvider.AddAttributes:
  res = layer.dataProvider().addAttributes( [ QgsField("mytext", QVariant.String), QgsField("myint", QVariant.Int) ] )

if caps & QgsVectorDataProvider.DeleteAttributes:
  res = layer.dataProvider().deleteAttributes( [ 0 ] )

# 4. using spatial index

# create spatial index
index = QgsSpatialIndex()

# add features to index
index.insertFeature(feat)

# query: returns array of feature IDs of five nearest features
nearest = index.nearestNeighbor(QgsPoint(25.4, 12.7), 5)

# query: returns array of IDs of features which intersect the rectangle
intersect = index.intersects(QgsRectangle(22.5, 15.3, 23.1, 17.2))

