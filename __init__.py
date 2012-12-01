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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "Pysal Tools"

def description():
  return "Pysal plugin for QGIS - dev"

def version(): 
  return "Version 0.1" 

def qgisMinimumVersion():
  return "1.0"

def icon():
	return "icons/default/pysal.png"

def classFactory(iface): 
  # load Pysal class from file Pysal
  from Pysal import Pysal 
  return Pysal(iface)
