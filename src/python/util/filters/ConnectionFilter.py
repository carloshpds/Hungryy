
# ===============================================
# Imports
# ===============================================
from cherrypy.filters.basefilter import BaseFilter
from cherrypy import request, session

# ===============================================
# ConnectionFilter class
# ===============================================
class ConnectionFilter(BaseFilter):
  """docstring for ConnectionFilter"""

  def before_request_body(self):
    try:

        if "skin" in request.params:
            skin       = request.params.pop("skin")
            connection = ConnectionFactory().getConnection()

    except Exception, exc:
      log.warning("Error in %s:\n%s", self.__class__.__name__, exc)
    