
# ===============================================
# Imports
# ===============================================
from src.python.util.factories.ConnectionFactory import ConnectionFactory
from src.python.food.FoodFactory import FoodFactory
from termcolor import colored

# ===============================================
# FoodDAO class
# ===============================================
class FoodDAO(object):

  """docstring for FoodDAO"""
  def __init__(self):
    self.connection  = ConnectionFactory().getConnection()
    self.connCursor  = self.connection.cursor()
    self.FoodFactory = FoodFactory()

  def listFoods(self):
    try:
      query = "SELECT * FROM food"
      self.connCursor.execute(query)

      results         = self.connCursor.fetchall()
      foodCollection  = self.FoodFactory.buildCollection(results)
      
      return foodCollection

    except Exception as error:
      print colored('[FoodDAO] listFoods: ' + str(error), 'red')

    finally:
      self.connection.close()


  def searchFoodByIngredients(self, ingredients=[]):
    try:
      ingredients = map(int, ingredients)
      ingredients = tuple(ingredients)

      query = """ SELECT * FROM food f 
                    WHERE f.id NOT IN (
                      SELECT fi.food_id FROM food_ingredient fi 
                      WHERE fi.ingredient_id NOT IN """ + str(ingredients) + """
                    )"""
      print colored(query, 'green')
      self.connCursor.execute(query)

      results         = self.connCursor.fetchall()
      foodCollection  = self.FoodFactory.buildCollection(results)
      
      return foodCollection

    except Exception as error:
      print colored('[FoodDAO] searchFoodByIngredients: ' + str(error), 'red')

    finally:
      self.connection.close()