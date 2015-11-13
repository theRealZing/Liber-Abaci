'''

 @author: Blair Elzinga
 create date: Nov 11, 2015

 module description:

'''

import math

class GoldFib(object):

  #def __init__(self):
    #instantiate nothing

  def fibList(self,n):
    """a constant order way to approximate a Fibonacci sequence number"""
    fiboList = []

    # don't process negative numbers
    if n < 0:
      return None

    # loop through the items
    for i in range(n):
      fiboList.append(self.fibAtN(i))
    return(fiboList)

  def fibAtN(self,n):
    # handle the start as a special case
    # start at 0
    if n > 2:
        return(int(math.floor(0.5+0.72360679774997896964091736687311*(1.6180339887498948482045868343656381177203**(n-1)))))
    elif n == 0:
        return(0)
    elif n == 1:
        return(1)
    elif n == 2:
        return(1)
    elif n < 0:
        return

  def fibFloor(self,point):
    fiboList = []

    # don't process negative numbers
    if point < 0:
      return fiboList

    # loop through the items
    n = 0
    x = self.fibAtN(n)
    while x < point:
      fiboList.append(x)
      n += 1
      x = self.fibAtN(n)
    return(fiboList)

  def fibCeil(self,point):
    fiboList = self.fibFloor(point)
    x = self.fibAtN(len(fiboList))
    fiboList.append(x)
    while x <= point:
      x = self.fibAtN(len(fiboList))
      fiboList.append(x)
    return(fiboList)


#for functional testing
if __name__ == '__main__':
  fib = GoldFib()
  print('floor sequence of 21 is '+str(fib.fibFloor(21)))
  print('ceil sequence of 21 is '+str(fib.fibCeil(21)))
  print('floor sequence of 22 is '+str(fib.fibFloor(22)))
  print('ceil sequence of 22 is '+str(fib.fibCeil(22)))
  nterms = int(input("How many terms? "))
  list1 = fib.fibList(nterms)
  for i in range(len(list1)):
    print (list1[i])

  print('at 5 is '+str(fib.fibAtN(5)))
  print('floor sequence of 1000 is '+str(fib.fibFloor(1000)))
  print('ceil sequence of 1000 is '+str(fib.fibCeil(1000)))
