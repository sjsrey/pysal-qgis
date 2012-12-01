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

from Ui_globalAuto import Ui_ga

class gaDialog(QDialog, Ui_ga):

  #def __init__(self,function):
  #  QDialog.__init__(self)
  #  self.function = function

  def __init__(self):
    QDialog.__init__(self)
    #self.function = function

  
  # run method that performs all the real work
  def globalMoran(self): 
    # create and show the dialog 
    #if function == 1:
    dlg = Ui_ga() 
      # show the dialog
    dlg.show()
    result = dlg.exec_() 
      # See if OK was pressed
    if result == 1: 
        # do something useful (delete the line containing pass and
        # substitute with your code
        pass 
    #else:
     # pass

  # run method that performs all the real work
  def globalGeary(self): 
    # create and show the dialog 
    if function == 2:
      dlg = Ui_ga() 
      # show the dialog
      dlg.show()
      result = dlg.exec_() 
      # See if OK was pressed
      if result == 1: 
        # do something useful (delete the line containing pass and
        # substitute with your code
        pass 
    else:
      pass

  # run method that performs all the real work
  def globalGetis(self): 
    # create and show the dialog 
    if function == 3:
      dlg = Ui_Dialog() 
      # show the dialog
      dlg.show()
      result = dlg.exec_() 
      # See if OK was pressed
      if result == 1: 
        # do something useful (delete the line containing pass and
        # substitute with your code
        pass 
    else:
      pass
