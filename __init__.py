"""
/***************************************************************************
Name			 	 : LISA for QGIS
Description          : Performs a LISA analysis using pysal
Date                 : 03/Nov/12 
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
  return "LISA for QGIS" 
def description():
  return "Performs a LISA analysis using pysal"
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "1.0"
def classFactory(iface): 
  # load lisa4qgis class from file lisa4qgis
  from lisa4qgis import lisa4qgis 
  return lisa4qgis(iface)

