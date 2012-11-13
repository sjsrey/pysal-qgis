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
from PysalDialog import PysalDialog

class Pysal: 

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface

  def initGui(self):  
    # Create action that will start plugin configuration
    self.action = QAction(QIcon(":/plugins/Pysal/icon.png"), \
        "Pysal", self.iface.mainWindow())
    # connect the action to the run method
    QObject.connect(self.action, SIGNAL("activated()"), self.run) 

    # Add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&Pysal", self.action)

    #Create new toolbar
    self.toolBar = self.iface.addToolBar("Pysal")
    self.toolBar.setObjectName("Pysal")
    
    # Create main Pysal menu and main Pysal subgroups, there is probably a more efficient way to do this
    self.menu = QMenu()
    esdaMenu = QMenu(self.menu)
    esdaMenu.setTitle("ESDA")
    weightsMenu = QMenu(self.menu)
    weightsMenu.setTitle("Weights")
    clusteringMenu = QMenu(self.menu)
    clusteringMenu.setTitle("Clustering")

    # add submenus under main Pysal menu
    self.menu.addMenu(esdaMenu)
    self.menu.addMenu(weightsMenu)
    self.menu.addMenu(clusteringMenu)
    self.menu.setTitle( QCoreApplication.translate( "Pysal","&Pysal" ) )
    lisa = QAction( QCoreApplication.translate("ESDA", "LISA" ), self.iface.mainWindow() )
    mat = QAction( QCoreApplication.translate("Weights","MAT" ), self.iface.mainWindow() )
    veroni = QAction( QCoreApplication.translate("Clustering","Veroni" ), self.iface.mainWindow() )
    
    # add actions to submenus, other actions will be added to the list here
    esdaMenu.addActions( [lisa] )
    weightsMenu.addActions( [mat] )
    clusteringMenu.addActions( [veroni] )

    menu_bar = self.iface.mainWindow().menuBar()
    actions = menu_bar.actions()
    lastAction = actions[ len( actions ) - 1 ]
    menu_bar.insertMenu( lastAction, self.menu )

    # assign methods to actions
    QObject.connect( lisa, SIGNAL("triggered()"), self.run )   
    QObject.connect( mat, SIGNAL("triggered()"), self.run )    
    QObject.connect( veroni, SIGNAL("triggered()"), self.run )  

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

# testing Venu's error message  
