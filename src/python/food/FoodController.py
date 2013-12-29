
# ===============================================
# Imports
# ===============================================
import cherrypy
from src.python.food.FoodDAO import FoodDAO
from src.python.util.factories.JSONSerializer import JSONSerializer

# ===============================================
# FoodController class
# ===============================================
class FoodController():

  def __init__(self):
    self.JSONSerializer = JSONSerializer()

  @cherrypy.expose
  def list(self):
    dao            = FoodDAO()
    foodCollection = dao.listFoods()

    return self.JSONSerializer.serialize(foodCollection)

  @cherrypy.expose
  def searchFoodByIngredients(self, ingredients):
    dao            = FoodDAO()
    foodCollection = dao.searchFoodByIngredients(ingredients)

    return self.JSONSerializer.serialize(foodCollection)

