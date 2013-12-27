
# ===============================================
# Imports
# ===============================================
from src.python.util.factories.ConnectionFactory import ConnectionFactory
from src.python.food.FoodFactory import FoodFactory

# ===============================================
# FoodDAO class
# ===============================================
class FoodDAO():

  """docstring for FoodDAO"""
  def __init__(self):
    self.connection  = ConnectionFactory().getConnection()
    self.connCursor  = self.connection.cursor()
    self.FoodFactory = FoodFactory()

  def listFoods(self):
    query = "SELECT * FROM food"
    self.connCursor.execute(query)

    results         = self.connCursor.fetchall()
    foodCollection  = self.FoodFactory.buildCollection(results)
    
    return foodCollection

  def searchFoodByIngredients(self, ingredients=[]):
    query = """ SELECT * FROM food f 
                  WHERE f.id NOT IN (
                    SELECT fi.food_id FROM food_ingredient fi 
                    WHERE fi.ingredient_id NOT IN """ + str(ingredients) + """
                  )"""

