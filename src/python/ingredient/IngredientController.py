
# ===============================================
# Imports
# ===============================================
import cherrypy
from src.python.ingredient.IngredientDAO import IngredientDAO
from src.python.util.factories.JSONSerializer import JSONSerializer

# ===============================================
# IngredientController class
# ===============================================
class IngredientController(object):
  """docstring for IngredientController"""
  
  def __init__(self):
    self.JSONSerializer = JSONSerializer()

  @cherrypy.expose
  def list(self):
    dao                   = IngredientDAO()
    ingredientsCollection = dao.listIngredients()
    return self.JSONSerializer.serialize(ingredientsCollection)