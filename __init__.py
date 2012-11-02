def name():
  return "My testing plugin"

def description():
  return "This plugin has no real use."

def version():
  return "Version 0.1"

def qgisMinimumVersion():
  return "1.0"

def authorName():
  return "Developer"

def classFactory(iface):
  # load TestPlugin class from file testplugin.py
  from testplugin import TestPlugin
  return TestPlugin(iface)
