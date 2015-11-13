'''

 @author: Blair Elzinga
 create date: Nov 12, 2015

 module description: unit tests for GoldFib module

'''

import unittest
from GoldFib import GoldFib

class TestGoldFib(unittest.TestCase):

  def test_fibAt0(self):
    fib = GoldFib()
    self.assertEqual(fib.fibAtN(0),0)

  def test_fibAt5(self):
    fib = GoldFib()
    self.assertEqual(fib.fibAtN(5),5)

  def test_seqNeg1(self):
    fib = GoldFib()
    self.assertEqual(fib.fibList(-3),None)

  def test_seq0(self):
    fib = GoldFib()
    self.assertEqual(fib.fibList(0),[])

  def test_seq1(self):
    fib = GoldFib()
    self.assertEqual(fib.fibList(1),[0])

  def test_seq5(self):
    fib = GoldFib()
    self.assertEqual(fib.fibList(5),[0,1,1,2,3])

  def test_floor(self):
    fib = GoldFib()
    self.assertEqual(fib.fibFloor(21),[0,1,1,2,3,5,8,13])

  def test_ceil(self):
    fib = GoldFib()
    self.assertEqual(fib.fibCeil(21),[0,1,1,2,3,5,8,13,21,34])


if __name__ == '__main__':
  unittest.main()
