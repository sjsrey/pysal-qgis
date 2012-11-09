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

# Identify the significant clusters at p=0.05
sig = lm.p_sim<0.05
print lm.p_sim[sig]

# Identify which quadrant each of these values is in
print lm.q[sig]

