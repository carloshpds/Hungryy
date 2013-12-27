
# ===============================================
# Imports
# ===============================================
import json

# ===============================================
# JSONSerializer class
# ===============================================
class JSONSerializer(object):
  """docstring for JSONSerializer"""

  def serialize(self, data):
    return json.dumps(data, default=lambda o: o.__dict__)
    