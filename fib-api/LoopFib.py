'''

 @author: Blair Elzinga
 create date: Nov 11, 2015

 module description:

'''

class LoopFib(object):

  def __init__(self):
    #instantiate an empty list
    self.fiboList = []

  def fibList(self,n):
    # don't process negative numbers
    if n < 0: return None

    index = len(self.fiboList)
    if index < n: #need to generate more terms
      # handle the start as a special case
      if index == 0 and n >= 1:
        self.fiboList.append(0)
        index+=1
      if index == 1 and n >= 2:
        self.fiboList.append(1)
        index+=1
      while index < n:
        self.fiboList.append(self.fiboList[index-2]+self.fiboList[index-1])
        index += 1
      return(self.fiboList)
    else:
      return(self.fiboList[0:n])

  def fibAtN(self,n):
    if len(self.fiboList) < n+1:
      x = self.fibList(n+1)
    index = len(self.fiboList)
    if index < n: 
      print 'idx:'+index
      print 'n:'+n
      x = self.fibList(n+2)
    return self.fiboList[n]

  def fibFloor(self,point):
    index = len(self.fiboList)
    # has the sequence generated already passed the point?
    if index > 1 and self.fibAtN(index-1) >= point:
      index-=1
      while(self.fibAtN(index-1) >= point):
        index-=1
      index+=1
    else:
      if index == 0:
        self.fiboList.append(0)
        index+=1
      if index == 1:
        self.fiboList.append(1)
        index+=1
   
      while point >= self.fiboList[index-1]+self.fiboList[index-2]:
        self.fiboList.append(self.fiboList[index-2]+self.fiboList[index-1])
        index += 1

    return(self.fiboList[0:index-1])

  def fibCeil(self,point):
    index = len(self.fiboList)
    if index > 1 and self.fibAtN(index-1) > point:
      index-=1
      while(self.fibAtN(index-1) > point):
        index-=1
      index+=1
    else:
      if index == 0:
        self.fiboList.append(0)
        index+=1
      if index == 1:
        self.fiboList.append(1)
        index+=1
   
      while point >= self.fiboList[index-1]:
        self.fiboList.append(self.fiboList[index-2]+self.fiboList[index-1])
        index += 1

    return(self.fiboList[0:index])

#for functional testing
if __name__ == '__main__':
  fibLoop = LoopFib()
  print('ceil sequence of 21 is '+str(fibLoop.fibCeil(21)))
  print('floor sequence of 21 is '+str(fibLoop.fibFloor(21)))
  print('floor sequence of 22 is '+str(fibLoop.fibFloor(22)))
  print('ceil sequence of 22 is '+str(fibLoop.fibCeil(22)))
  nterms = int(input("How many terms? "))

  print('at '+str(nterms)+' is '+str(fibLoop.fibAtN(nterms)))

  print('floor sequence of 73 is '+str(fibLoop.fibFloor(73)))
  print('ceil sequence of 73 is '+str(fibLoop.fibCeil(73)))
  print('longer list '+str(fibLoop.fibList(15)))
  print('shorter list '+str(fibLoop.fibList(10)))

  list1 = fibLoop.fibList(nterms)
  for i in range(len(list1)):
    print (list1[i])

