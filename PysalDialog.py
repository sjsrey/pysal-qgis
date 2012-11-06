"""
/***************************************************************************
Name			 	 : Pysal Tools
Description          : Pysal plugin for QGIS
Date                 : 06/Nov/12 
copyright            : (C) 2012 by ASU's GPH 498/598
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
from Ui_Pysal import Ui_Pysal
# create the dialog for Pysal
class PysalDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_Pysal ()
    self.ui.setupUi(self)