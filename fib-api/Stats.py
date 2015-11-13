'''

 @author: Blair Elzinga
 create date: Nov 11, 2015

 module description:

'''

class Stats:
  def __init__(self):
    self.endpoints = {}

  def start(self,uri,start):
    if self.endpoints.has_key(uri):
      self.endpoints[uri] += 1
    else:
      #create a new entry
      self.endpoints[uri] = 1

  def finish(self,uri, finish, status):
    pass

  def getInvocationCount(self,uri):
    return self.endpoints.get(uri)

  def getStats(self):
    return self.endpoints
