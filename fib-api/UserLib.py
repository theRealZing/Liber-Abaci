'''

 @author: Blair Elzinga
 create date: Nov 11, 2015

 module description:

'''

class UserLib(object):

  def __init__(self):
    self.fibLibrary = {}

  def add(self,className,description):
    if self.fibLibrary.has_key(className):
      raise ValueError('class already in library')
      return
    self.fibLibrary[className] = description
    return

  def delete(self,className):
    if not self.fibLibrary.has_key(className):
      raise ValueError("class not in library")
      return
    del self.fibLibrary[className]
    return

  def update(self,className,description):
    if not self.fibLibrary.has_key(className):
      raise ValueError("class not in library")
      return
    self.fibLibrary[className] = description
    return

  def getList(self):
    return self.fibLibrary.values()

  def list(self):
    return self.fibLibrary
