
# ===============================================
# Imports
# ===============================================
from src.python.ingredient.Ingredient import Ingredient
from src.python.util.factories.EntityFactory import EntityFactory

# ===============================================
# IngredientFactory class
# ===============================================
class IngredientFactory(EntityFactory):

  def buildObject(self, item):
    ingredientObject = Ingredient(
      id          = int(item[0]), 
      name        = item[1]         
    )
    return ingredientObject 