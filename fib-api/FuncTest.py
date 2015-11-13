'''

 @author: Blair Elzinga
 create date: Nov 11, 2015

 module description: allow API users to run functional tests that
 compare Fibonacci routines for accuracy and speed.

  This is useful for design documentation, but isn't necessary for execution
  def initDict(self,dict1):
    dict1['sequence 10']=None
    dict1['sequence 50']=None
    dict1['sequence 100']=None
    dict1['sequence 500']=None
    dict1['starts at 0']=None
    dict1['value at 5']=None
    dict1['value at 200']=None
    dict1['floor of 1000']=None
    dict1['ceil of 1000']=None
    dict1['time of basic tests']=None
    dict1['sequence speed tests']=None
    dict1['value speed tests']=None
    dict1['floor speed tests']=None
    dict1['ceiling speed tests']=None
    return dict1
'''
import timeit
import time

class FuncTest(object):

  def __init__(self):
    #hold results for test set 1
    self.standard = {}

    #hold results for test set 2
    self.sut = {}
   
    #hold results for test comparisons
    self.result = {}

    self.standardLibrary = None
    self.testLibrary = None
    self.testPass = True


  def getStandardDictionary(self):
    return self.standard

  def getTestDictionary(self):
    return self.sut

  def runLibraryTests(self,fibLibrary,resultDictionary):
    try:
      resultDictionary[' library'] = fibLibrary
      startTime = time.clock()
      methodLoad = __import__(fibLibrary)
      dynLoad = 'methodLoad.'+fibLibrary+'()'
      fibLib = eval(dynLoad)
      resultDictionary['sequence 10'] = fibLib.fibList(10)
      resultDictionary['sequence 50'] = fibLib.fibList(50)
      resultDictionary['sequence 100'] = fibLib.fibList(100)
      resultDictionary['sequence 500'] = fibLib.fibList(500)
      resultDictionary['starts at 0'] = fibLib.fibAtN(0)
      resultDictionary['value at 5'] = fibLib.fibAtN(5)
      resultDictionary['value at 200'] = fibLib.fibAtN(200)
      resultDictionary['floor of 1000'] = fibLib.fibFloor(1000)
      resultDictionary['ceil of 1000'] = fibLib.fibCeil(1000)
      ss = "fib=__import__('"+fibLibrary+"'); fibLib=fib."+fibLibrary+'()'
      resultDictionary['sequence speed tests'] = timeit.timeit('fibLib.fibList(311)', setup=ss ,number = 5000)
      resultDictionary['value speed tests']=timeit.timeit('fibLib.fibAtN(311)', setup=ss, number = 5000)
      resultDictionary['floor speed tests']=timeit.timeit('fibLib.fibFloor(311)', setup=ss, number = 5000)
      resultDictionary['ceiling speed tests']=timeit.timeit('fibLib.fibCeil(311)', setup=ss, number = 5000)
      stopTime = time.clock()
      resultDictionary['time of basic tests'] = stopTime - startTime
    except:
      return('exception')
    else:
      return('tests worked')

  def showBoth(self,key):
    if (self.standard.has_key(key)): standard = str(self.standard[key])
    else: standard = 'missing'
    if (self.sut.has_key(key)): sut = str(self.sut[key])
    else: sut = 'missing'
    self.result[key] = 'standard:'+standard+'  underTest:'+sut
    if standard == 'missing' and sut == 'missing':
      self.testPass = False

  def compare(self):
    self.showBoth(' library')
    self.showBoth('time of basic tests')
    self.showBoth('sequence speed tests')
    self.showBoth('value speed tests')
    self.showBoth('floor speed tests')
    self.showBoth('ceiling speed tests')
    self.compareSequence('sequence 10')
    self.compareSequence('sequence 50')
    self.compareSequence('sequence 100')
    self.compareSequence('sequence 500')
    self.compareValue('starts at 0')
    self.compareValue('value at 5')
    self.compareValue('value at 200')
    self.compareSequence('floor of 1000')
    self.compareSequence('ceil of 1000')
    return self.result

  def compareSequence(self,key):
    # sequences are lists
    if (self.standard.has_key(key)):
      stdSeq = self.standard[key]
    else:
      stdSeq = []
    if (self.sut.has_key(key)):
      sutSeq = self.sut[key]
    else:
      sutSeq = []
    if stdSeq == [] and sutSeq == []:
      self.result[key] = 'standard:missing  underTest:missing'
      self.testPass = False
      return
    
    if len(stdSeq) != len(sutSeq):
      self.result[key] = 'unequal length: standard:'+str(len(stdSeq))+'  underTest:'+str(len(sutSeq))
      self.testPass = False
    elif stdSeq == sutSeq:
      self.result[key] = 'equal'
    else:
      self.result[key] = 'not equal, elements of sequence differ in value'
      self.testPass = False
      
  def compareValue(self,key):
    if (self.standard.has_key(key)):
      stdVal = self.standard[key]
    else:
      stdVal = -99
    if (self.sut.has_key(key)):
      sutVal = self.sut[key]
    else:
      sutVal = -99
    if stdVal == -99 and sutVal == -99:
      self.result[key] = 'standard:missing  underTest:missing'
      self.testPass = False
      return
    # values are ints
    if stdVal == sutVal:
      self.result[key] = 'equal'
    else:
      self.result[key] = 'not equal: expected:'+str(stdVal)+' actual:'+str(sutVal)
      self.testPass = False
      
  def testsPassed(self):
    return self.testPass

if __name__ == '__main__':
  tests = FuncTest()
  stdLib = tests.getStandardDictionary()
  tests.runLibraryTests('TableFib',stdLib)
  #print str(stdLib)
  tstLib = tests.getTestDictionary()
  tests.runLibraryTests('GoldFib',tstLib)
  #print str(tstLib)
  #print str(tests.compare())
  for key, value in sorted(tests.compare().iteritems()):
    print str(key)+": "+str(value)

  if tests.testsPassed() == True: print "Library passed"
  else: print "Library failed"
  
