from data.DbHelper import DbHelper

class ArchiveDao(object):
   __db = None;
    
   def __init__(self):
      self.__db = DbHelper('clients.db')
      self.__db.query("CREATE TABLE IF NOT EXISTS ClientArchives (id INTEGER PRIMARY KEY AUTOINCREMENT, hostname TEXT, lastActiveTime TIMESTAMP)",{})
   
   def addArchive(self, archive):
      self.__db.query("INSERT INTO ClientArchives (hostname, lastActiveTime) VALUES(:hostname,:lastActiveTime)",archive)
      