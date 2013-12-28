
# ===============================================
# Imports
# ===============================================
import cherrypy

from Root import Root
from src.python.food.FoodController import FoodController
from src.python.ingredient.IngredientController import IngredientController

# ===============================================
# Main
# ===============================================
if __name__ == '__main__':

  rootPage      		= Root()
  rootPage.food 		= FoodController()
  rootPage.ingredient	= IngredientController()

  cherrypy.quickstart(rootPage, '/api', config=rootPage.config)