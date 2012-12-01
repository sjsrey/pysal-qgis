import numpy as np
import pysal

# Open the dbf associated with your shapefile
db = pysal.open('Iowa.dbf')

# Select the attribute you want to observe
y = np.array(db.by_col['GOVTPAYPER'])

# Create a weights matrix for this session (or, open existing one)
w = pysal.queen_from_shapefile('Iowa.shp',idVariable='POLY_ID')

# Command for Moran's Local
np.random.seed(12345)
lm = pysal.Moran_Local(y,w)

# Replace insignificant values with the number 5:
for i in range(len(lm.p_sim)):
	if lm.p_sim[i] > 0.05:
		lm.p_sim[i] = 5 

# Replace the significant values with their quadrant:
for i in range(len(lm.p_sim)):
	if lm.p_sim[i] <= 0.05:
		lm.p_sim[i] =lm.q[i] 
print lm.p_sim

""" If needed, zip the id variable and the output variable into a list:
id = np.array(db.by_col['POLY_ID'])
idsig = zip(id,lm.p_sim)
print idsig 
"""

