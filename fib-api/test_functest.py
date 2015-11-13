'''

 @author: Blair Elzinga
 create date: Nov 12, 2015

 module description: unit tests for FuncTest module

'''

import unittest
from FuncTest import FuncTest

class TestFuncTest(unittest.TestCase):
  def setUp(self):
    pass

  def test_compare(self):
    tests = FuncTest()
    stdLib = tests.getStandardDictionary()
    tests.runLibraryTests('TableFib',stdLib)
    tstLib = tests.getTestDictionary()
    tests.runLibraryTests('TableFib',tstLib)

    self.assertEqual(tests.testsPassed(),True)

  def test_compare2(self):
    tests = FuncTest()
    stdLib = tests.getStandardDictionary()
    tests.runLibraryTests('LoopFib',stdLib)
    tstLib = tests.getTestDictionary()
    tests.runLibraryTests('GoldFib',tstLib)

    self.assertEqual(tests.testsPassed(),True)

if __name__ == '__main__':
  tests = FuncTest()
  unittest.main()
