'''

 @author: Blair Elzinga
 create date: Nov 11, 2015

 module description:

'''

class TableFib(object):

  def __init__(self):
    # initialize a small table
    self.fibTable = {0:0, 1:1, 2:1}

  def fibAtN(self,n):
    if n in self.fibTable: #already have it calculated, just return it
      return self.fibTable[n]
    else: #add a new value
      self.fibTable[n] = self.fibAtN(n-1)+self.fibAtN(n-2) #limited recursion
      return self.fibTable[n]

  def fibList(self,n):
    if n < 0: return None
    if n == 0: return []
    if n == 1: return [0]
    x = self.fibAtN(n-1)
    return self.fibTable.values()

  def fibFloor(self,point):
    if point < 0: return None
    n = 0
    x = self.fibAtN(n)
    while x < point:
      n += 1
      x = self.fibAtN(n)
    return((self.fibTable.values())[0:n])

  def fibCeil(self,point):
    if point < 0: return [0]
    n = 0
    x = self.fibAtN(n)
    while x <= point:
      n += 1
      x = self.fibAtN(n)
    n += 1
    x = self.fibAtN(n)
    return((self.fibTable.values())[0:n])
    

#for functional testing
if __name__ == '__main__':
  fib = TableFib()
  nterms = int(input("How many terms? "))
  list1 = fib.fibList(nterms)
  for i in range(len(list1)):
    print (list1[i])
  print('at 5 is '+str(fib.fibAtN(5)))
  print('floor sequence of 1000 is '+str(fib.fibFloor(1000)))
  print('ceil sequence of 1000 is '+str(fib.fibCeil(1000)))
  print('floor sequence of 21 is '+str(fib.fibFloor(21)))
  print('ceil sequence of 21 is '+str(fib.fibCeil(21)))
