
# ===============================================
# EntityFactory class
# ===============================================
class EntityFactory(object):
  """docstring for EntityFactory"""
  
  def buildObject(self, item):
    raise NotImplementedError('This method [EntityFactory: buildObject] should be overridden.')

  def buildCollection(self, collection):
    ObjectCollection = []

    for item in collection:
      instance = self.buildObject(item)
      ObjectCollection.append(instance)

    return ObjectCollection