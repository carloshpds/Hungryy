
# ===============================================
# Imports
# ===============================================
from src.python.util.factories.ConnectionFactory import ConnectionFactory
from src.python.recipe.RecipeFactory import RecipeFactory
from termcolor import colored

# ===============================================
# RecipeDAO class
# ===============================================
class RecipeDAO(object):

  """docstring for RecipeDAO"""
  def __init__(self):
    self.connection  = ConnectionFactory().getConnection()
    self.connCursor  = self.connection.cursor()
    self.recipeFactory = RecipeFactory()

  def listRecipes(self):
    try:
      query = "SELECT * FROM recipe"
      self.connCursor.execute(query)

      results           = self.connCursor.fetchall()
      recipeCollection  = self.recipeFactory.buildCollection(results)
      
      return recipeCollection

    except Exception as error:
      print colored('[RecipeDAO] listFoods: ' + str(error), 'red')

    finally:
      self.connection.close()


  def searchRecipeByIngredients(self, ingredientsIds=[]):
    try:
      ingredientsIds = map(int, ingredientsIds)
      ingredientsIds = tuple(ingredientsIds)

      query = """ SELECT * FROM recipe r
                    WHERE r.id NOT IN (
                      SELECT ri.food_id FROM recipe_ingredient ri 
                      WHERE ri.ingredient_id NOT IN """ + str(ingredientsIds) + """
                    )"""
      print colored(query, 'green')
      self.connCursor.execute(query)

      results           = self.connCursor.fetchall()
      recipeCollection  = self.recipeFactory.buildCollection(results)
      
      return recipeCollection

    except Exception as error:
      print colored('[RecipeDAO] searchFoodByIngredients: ' + str(error), 'red')

    finally:
      self.connection.close()