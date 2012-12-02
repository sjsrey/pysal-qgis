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
from PyQt4 import QtCore, QtGui 
from globalgeary import Ui_globalgeary
# create the dialog for ga
class globalgDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_globalgeary()
    self.ui.setupUi(self)
