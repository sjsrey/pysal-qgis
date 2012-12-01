import pysal as PS
import numpy as NP

def contiguity_from_shapefile(shapefile, criteria='rook'):
    """
    Create a spatial weights object based on a contiguity criteria from a
    shapefile.

    Produces a "*.gal" file in the directory of the shapefile


    Argument
    --------
    shapefile: string with full path to shapefile

    criteria: string for type of contiguity ['rook'|'queen']

    Returns
    -------
    cards: nx1 numpy array with the number of neighbors for each element based
    on criterion

    """

    if criteria == 'rook':
        PS.rook_from_shapefile(shapefile)
        abb = 'r'
    else:
        PS.queen_from_shapefile(shapefile)
        abb = 'q'
    cards = NP.array(w.cardinalities.values())
    cards.shape = (len(cards),1)
    galfile = shapefile.split(".")[0] + "_" + abb + ".gal"
    gal = PS.open(galfile,'w')
    gal.write(w)
    gal.close()

    return cards
