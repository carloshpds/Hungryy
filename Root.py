
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
   
  @cherrypy.expose
  def index(self):
    return serve_file(os.path.join(public_dir , 'index.html'), content_type='text/html')