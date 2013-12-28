
# ===============================================
# Imports
# ===============================================
from src.python.food.Food import Food
from src.python.util.factories.EntityFactory import EntityFactory

# ===============================================
# FoodFactory class
# ===============================================
class FoodFactory(EntityFactory):

  def buildObject(self, item):
    foodObject = Food(
      id          = int(item[0]), 
      name        = item[1],      
      description = item[2]      
    )
    return foodObject 
