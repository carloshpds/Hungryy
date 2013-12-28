
# ===============================================
# Imports
# ===============================================
from src.python.util.factories.ConnectionFactory import ConnectionFactory
from src.python.ingredient.IngredientFactory import IngredientFactory

# ===============================================
# IngredientDAO class
# ===============================================
class IngredientDAO(object):

  """docstring for IngredientDAO"""
  def __init__(self):
    self.connection        = ConnectionFactory().getConnection()
    self.connCursor        = self.connection.cursor()
    self.IngredientFactory = IngredientFactory()

  def listIngredients(self):
    try:
      query = "SELECT * FROM ingredient"
      self.connCursor.execute(query)

      results         = self.connCursor.fetchall()
      foodCollection  = self.IngredientFactory.buildCollection(results)
    
      return foodCollection

    except Exception as error:
      print '[IngredientDAO] listIngredients: ' + str(error)