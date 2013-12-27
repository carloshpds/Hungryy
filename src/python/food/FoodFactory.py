
# ===============================================
# Imports
# ===============================================
from src.python.food.Food import Food

# ===============================================
# FoodFactory class
# ===============================================
class FoodFactory():

  def buildObject(self, item):
    foodObject = Food(
      id          = int(item[0]), #id
      name        = item[1],      #name
      description = item[2]       #description
    )
    return foodObject 

  def buildCollection(self, collection):
    foodCollection = []

    for item in collection:
      food = self.buildObject(item)
      foodCollection.append(food)

    return foodCollection