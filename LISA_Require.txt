NEEDS for LISA Plugin:

1.) User selects a shapefile
2.) User selects a variable/attribute of interest
3.) User selects or creates a weights matrix
4.) User selects (or is told) a significance value
5.) autocorrelation output is appended to the QGIS attribute table


WANTS/details:

1.) Select shapefile

2.) Variable/attribute selection
	Read attributes (db.header in pysal) 

3.) Weights matrix
	Definitely should have:	
		knn - can probably use centroid dist. in pysal
		queen/rook contiguity - use pysal or figure out how to do in qgis?
		threshold distance - can probably use centroid dist. in pysal

4.) Significance Value
	Each p-value would be its own new attribute column

5.) Append to attribute table
	write to DBF?
	Numpy array is [1,2,3,4].  Should we change to [HH,HL,LL,LH] ?
	Output preview?  Useful to avoid "junk output" gets appended to dbf
	Append name of weights matrix/sig level to new attribute!!
		i.e, 	(LISA_) + (nn4_) + (05)
			(LISA_) + (Queen1_) + (01)
			(LISA_) + (thresh200_) + (10)
	Automatic display/color scheme possible in QGIS?
