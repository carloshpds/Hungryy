
# ===============================================
# Imports
# ===============================================
import cherrypy
import os.path
import json
import time

from Root import Root

# ===============================================
# Global variables
# ===============================================
current_dir = os.path.dirname(os.path.abspath(__file__))
public_dir  = os.path.join(current_dir, 'public/dist')


# ===============================================
# Main
# ===============================================
if __name__ == '__main__':

  pageroot = Root()

  conf = {
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


  cherrypy.quickstart(pageroot, '/api', config=conf)