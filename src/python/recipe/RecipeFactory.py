
# ===============================================
# Imports
# ===============================================
from src.python.recipe.Recipe import Recipe
from src.python.util.factories.EntityFactory import EntityFactory

# ===============================================
# RecipeFactory class
# ===============================================
class RecipeFactory(EntityFactory):

  def buildObject(self, item):
    recipeObject = Recipe(
      id          = int(item[0]), 
      name        = item[1],      
      description = item[2]      
    )
    return recipeObject 

