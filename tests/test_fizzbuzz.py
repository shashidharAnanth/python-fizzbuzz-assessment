import unittest
from fizzbuzz import fizzbuzz

class FizzbuzzTest(unittest.TestCase):

  def testFizzBuzzPositiveNumbers(self):
    self.assertEqual("12", fizzbuzz(1,2))
    self.assertEqual("12Fizz", fizzbuzz(1,3))
    self.assertEqual("12Fizz4Buzz", fizzbuzz(1,5))
    self.assertEqual("BuzzFizz78FizzBuzz11Fizz1314FizzBuzz", fizzbuzz(5,15))

  def testFizzBuzzNegativeNumbers(self):
    self.assertEqual("-2-1", fizzbuzz(-2,-1))
    self.assertEqual("Fizz-2-1", fizzbuzz(-3,-1))
    self.assertEqual("Buzz-4Fizz-2-1", fizzbuzz(-5,-1))
    self.assertEqual("FizzBuzz-14-13Fizz-11BuzzFizz-8-7FizzBuzz", fizzbuzz(-15,-5))

  def testFizzBuzzPositiveAndNegativeNumbers(self):
    self.assertEqual("Fizz-2-1FizzBuzz12Fizz", fizzbuzz(-3,3))
    self.assertEqual("FizzBuzz-14-13Fizz-11BuzzFizz-8-7FizzBuzz-4Fizz-2-1FizzBuzz12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz", fizzbuzz(-15,15))

  def testFizzBuzzOneToTwenty(self):
    self.assertEqual("12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617Fizz19Buzz", fizzbuzz(1,20))