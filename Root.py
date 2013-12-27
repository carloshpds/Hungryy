
# ===============================================
# Imports
# ===============================================
import cherrypy
import os.path
import json
import time
from cherrypy.lib.static import serve_file


# ===============================================
# Global variables
# ===============================================
current_dir = os.path.dirname(os.path.abspath(__file__))
public_dir  = os.path.join(current_dir, 'public/dist')


# ===============================================
# Root Class
# ===============================================
class Root():
   
  def __init__(self):
    self.config = {
      '/' : {
        'tools.encode.encoding': 'utf-8',
        'response.timeout' :  1000000,
        'tools.staticdir.root': current_dir
      },

      '/api' : {
        'tools.encode.encoding': 'utf-8',
        'response.timeout' :  1000000,
        'tools.staticdir.root': current_dir
      },

      '/feed': {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir': os.path.join(current_dir, 'public'),
        'tools.staticdir.content_types': {
          'rss' : 'application/json',
          'atom': 'application/json'
        },
        
      },

      '/scripts' : {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir': os.path.join(public_dir,'scripts' )
      },

      '/styles' : {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir': os.path.join(public_dir,'styles' )
      },

      '/views' : {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir': os.path.join(public_dir, 'views' )
      }
    }

  @cherrypy.expose
  def index(self):
    return serve_file(os.path.join(public_dir , 'index.html'), content_type='text/html')