
# ===============================================
# Imports
# ===============================================
import MySQLdb

# ===============================================
# ConnectionFactory class
# ===============================================
class ConnectionFactory(object):

  def __init__(self):
    self.connectionConfig = {
      'user'   : 'hungryy-user',
      'passwd' : 'hungryy-db',
      'host'   : 'localhost',
      'db'     : 'hungryy-db'
    }


  def getConnection(self):
    
    try:
      connection = MySQLdb.connect(
        host    = self.connectionConfig['host'],
        user    = self.connectionConfig['user'],
        passwd  = self.connectionConfig['passwd'],
        db      = self.connectionConfig['db']
      )
      return connection

    except MySQLdb.Error as err:
      print err