
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
    # print 'Food listMethod'
    dao            = FoodDAO()
    foodCollection = dao.listFoods()
    dao.connection.close()

    return self.JSONSerializer.serialize(foodCollection)

