"""
/***************************************************************************
Name			 	 : Pysal Tools
Description          : Pysal plugin for QGIS
Date                 : 06/Nov/12 
copyright            : (C) 2012 by ASU's GPH 498/598
email                :  
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
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog

import sys, os

currentPath = os.path.dirname( __file__ )
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/ga'))

from PysalDialog import PysalDialog
from gaDialog import gaDialog
class Pysal: 

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface

  def initGui(self):  
    # Create action that will start plugin configuration
    self.action = QAction(QIcon("home/everett/.qgis/python/plugins/Pysal/pysal.png"), \
        "PySAL", self.iface.mainWindow())
    # connect the action to the run method
    QObject.connect(self.action, SIGNAL("activated()"), self.run) 

    # Add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&PySAL", self.action)

    #Create new toolbar
    self.toolBar = self.iface.addToolBar("PySAL")
    self.toolBar.setObjectName("PySAL")
    
    # Create main Pysal menu and main Pysal subgroups, there is probably a more efficient way to do this
    self.menu = QMenu()
    esdaMenu = QMenu(self.menu)
    esdaMenu.setTitle("ESDA")
    weightsMenu = QMenu(self.menu)
    weightsMenu.setTitle("Weights")
    localAutoMenu = QMenu(esdaMenu)
    localAutoMenu.setTitle("Local Autocorrelation")
    globalAutoMenu = QMenu(esdaMenu)
    globalAutoMenu.setTitle("Global Autocorrelation")

    # add submenus under main Pysal menu
    self.menu.addMenu(esdaMenu)
    self.menu.addMenu(weightsMenu)
    esdaMenu.addMenu(globalAutoMenu)
    esdaMenu.addMenu(localAutoMenu)
    self.menu.setTitle( QCoreApplication.translate( "PySAL","&PySAL" ) )
    moransGlobal = QAction(QIcon("home/everett/.qgis/python/plugins/Pysal/pysal.png"), QCoreApplication.translate("Global Autocorrelation", "Moran's I" ), self.iface.mainWindow() )
    moransLocal = QAction(QIcon("~/.qgis/python/plugins/Pysal/pysal.png"), QCoreApplication.translate("Local Autocorrelation", "Moran's I" ), self.iface.mainWindow() )
    gearys = QAction( QCoreApplication.translate("Global Autocorrelation","Geary's C"),self.iface.mainWindow() )
    getis = QAction( QCoreApplication.translate("Global Autocorrelation","Getis and Ord's G"),self.iface.mainWindow() )
    mat = QAction( QCoreApplication.translate("Weights","MAT" ), self.iface.mainWindow() )
        
    # add actions to submenus, other actions will be added to the list here
    localAutoMenu.addActions( [moransLocal] )
    globalAutoMenu.addActions( [moransGlobal,gearys,getis] )
    weightsMenu.addActions( [mat] )

    menu_bar = self.iface.mainWindow().menuBar()
    actions = menu_bar.actions()
    lastAction = actions[ len( actions ) - 1 ]
    menu_bar.insertMenu( lastAction, self.menu )

    # assign methods to actions
    QObject.connect( moransLocal, SIGNAL("triggered()"), self.run )   
    QObject.connect( moransGlobal, SIGNAL("triggered()"), self.globalMoran )
    QObject.connect( mat, SIGNAL("triggered()"), self.run )    
    QObject.connect( gearys, SIGNAL("triggered()"), self.globalGeary )  
    QObject.connect( getis, SIGNAL("triggered()"), self.globalGetis )

  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("&Pysal",self.action)
    self.iface.removeToolBarIcon(self.action)
    del self.toolBar
    del self.menu

  # run method that performs all the real work
  def run(self): 
    # create and show the dialog 
    dlg = PysalDialog() 
    # show the dialog
    dlg.show()
    result = dlg.exec_() 
    # See if OK was pressed
    if result == 1: 
      # do something useful (delete the line containing pass and
      # substitute with your code
      pass
 
  # run method that performs all the real work
  def globalMoran(self): 
    # create and show the dialog 
    dlg1 = gaDialog() 
    # show the dialog
    dlg1.show()
    result = dlg1.exec_() 
    # See if OK was pressed
  # run method that performs all the real work
  def globalGeary(self): 
    # create and show the dialog 
    dlg1 = gaDialog()
    # show the dialog
    dlg1.show()
    result = dlg1.exec_() 
    # See if OK was pressed


  # run method that performs all the real work
  def globalGetis(self): 
    # create and show the dialog 
    dlg1 = gaDialog() 
    # show the dialog
    dlg1.show()
    result = dlg1.exec_() 
    # See if OK was pressed

### testing Venu's error message  
