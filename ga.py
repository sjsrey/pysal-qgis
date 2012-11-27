"""
/***************************************************************************
Name			 	 : Global Autocorrelation
Description          : Global Autocorrelation module
Date                 : 13/Nov/12 
copyright            : (C) 2012 by ASU
email                : x 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *

from gaDialog import gaDialog

class ga: 
  
  # run method that performs all the real work
  def globalMoran(self): 
    # create and show the dialog 
    dlg = gaDialog() 
    # show the dialog
    dlg.show()
    result = dlg.exec_() 
    # See if OK was pressed
    if result == 1: 
      # do something useful (delete the line containing pass and
      # substitute with your code
      pass 

  # run method that performs all the real work
  def globalGeary(self): 
    # create and show the dialog 
    dlg = gaDialog() 
    # show the dialog
    dlg.show()
    result = dlg.exec_() 
    # See if OK was pressed
    if result == 1: 
      # do something useful (delete the line containing pass and
      # substitute with your code
      pass 

  # run method that performs all the real work
  def globalGetis(self): 
    # create and show the dialog 
    dlg = gaDialog() 
    # show the dialog
    dlg.show()
    result = dlg.exec_() 
    # See if OK was pressed
    if result == 1: 
      # do something useful (delete the line containing pass and
      # substitute with your code
      pass 
