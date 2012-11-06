"""
/***************************************************************************
Name			 	 : LISA for QGIS
Description          : Performs a LISA analysis using pysal
Date                 : 03/Nov/12 
copyright            : (C) 2012 by GPH 498/598
email                : gel@asu.edu 
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
from Ui_lisa4qgis import Ui_lisa4qgis
# create the dialog for lisa4qgis
class lisa4qgisDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_lisa4qgis ()
    self.ui.setupUi(self)
