'''

 @author: Blair Elzinga
 create date: Nov 12, 2015

 module description: unit tests for Stats module

'''

import unittest
from Stats import Stats

class TestStats(unittest.TestCase):
  def setUp(self):
    pass

  def test_start(self):
    testStats = Stats()
    testStats.start('one','two')
    mockStats = {}
    mockStats['one'] = 1
    self.assertEqual(testStats.getStats(),mockStats)

  def test_finish(self):
    pass

  def test_getInvocationCount(self):
    testStats = Stats()
    testStats.start('two','three')
    self.assertEqual(testStats.getInvocationCount('two'),1)
    testStats.start('two','four')
    self.assertEqual(testStats.getInvocationCount('two'),2)

  def test_getStats(self):
    pass

if __name__ == '__main__':
  unittest.main()
