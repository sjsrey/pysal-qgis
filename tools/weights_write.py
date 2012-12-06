    def contiguity_from_shapefile(shapefile, criteria='rook'):
        if criteria == 'rook':
	    w = PS.rook_from_shapefile(shapefile)
            abb = 'r'
    	else:
            w = PS.queen_from_shapefile(shapefile)
            abb = 'q'
    	    cards = NP.array(w.cardinalities.values())
    	    cards.shape = (len(cards),1)
    	    att_name = shapefile.split(".")[0] + "_" + abb
	    layer = QgsVectorLayer(shapefile,"shapefile","ogr")
	    provider = layer.dataProvider()
	    feat = QgsFeature()
	    caps = layer.dataProvider().capabilities()
	    if caps & QgsVectorDataProvider.AddAttributes:
		res = layer.dataProvider().addAttributes([QgsField(att_name,QVariant.Int)]
	    a = range(layer.featureCount())
	    d = dict(zip(a,cards)
	    allAtt = provider.attributeIndexes()
	    n = len(allAtt) - 1
	    for i in a:
		fid = i
		if caps & QgsVectorDataProvider.ChangeAttributeValues:
		    attrs = {n : QVariant(d[i])}
		    layer.dataProvider().changeAttributeValues({fid:attrs})


