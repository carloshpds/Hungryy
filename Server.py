
# ===============================================
# Imports
# ===============================================
import cherrypy

from Root import Root
from src.python.food.FoodController import FoodController

# ===============================================
# Main
# ===============================================
if __name__ == '__main__':

  rootPage      = Root()
  rootPage.food = FoodController()

  cherrypy.quickstart(rootPage, '/api', config=rootPage.config)