'''

 @author: Blair Elzinga
 create date: Nov 12, 2015

 module description: unit tests for UserLib module

'''

import unittest
from UserLib import UserLib

class TestUserLib(unittest.TestCase):

  def setUp(self):
    self.userLib = UserLib()

  def test_add1(self):
    self.userLib.add('one','two')
    self.assertEqual(self.userLib.list(),{'one':'two'})
  def test_add2(self):
    self.userLib.add('one','two')
    self.userLib.add('three','four')
    self.assertEqual(self.userLib.list(),{'one':'two','three':'four'})
  def test_addDuplicate(self):
    self.userLib.add('one','two')
    self.assertRaises(ValueError,self.userLib.add,'one','five')

  def test_delete(self):
    self.userLib.add('one','two')
    self.userLib.add('three','four')
    self.userLib.delete('one')
    self.assertEqual(self.userLib.list(),{'three':'four'})
  def test_badDelete(self):
    self.userLib.add('three','four')
    self.assertRaises(ValueError,self.userLib.delete,'deleteMe')

  def test_update(self):
    self.userLib.add('three','four')
    self.userLib.update('three','funkiness reigns')
    self.assertEqual(self.userLib.list(),{'three':'funkiness reigns'})
  def test_badUpdate(self):
    self.userLib.add('three','four')
    self.assertRaises(ValueError,self.userLib.update,'foo','bar')

if __name__ == '__main__':
  unittest.main()
