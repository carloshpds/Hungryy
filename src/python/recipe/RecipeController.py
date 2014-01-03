
# ===============================================
# Imports
# ===============================================
import cherrypy
from src.python.recipe.RecipeDAO import RecipeDAO
from src.python.util.factories.JSONSerializer import JSONSerializer

# ===============================================
# RecipeController class
# ===============================================
class RecipeController():

  def __init__(self):
    self.JSONSerializer = JSONSerializer()

  @cherrypy.expose
  def list(self):
    dao              = RecipeDAO()
    recipeCollection = dao.listRecipes()

    return self.JSONSerializer.serialize(recipeCollection)

  @cherrypy.expose
  def searchRecipeByIngredients(self, ingredientsIds):
    dao            = RecipeDAO()
    recipeCollection = dao.searchRecipeByIngredients(ingredientsIds)

    return self.JSONSerializer.serialize(recipeCollection)

