# def do_stuff(num=0):
#   try:
#     if num:
#       return int(num) + 5
#     else: 
#       return 'Please enter a number'
#   except ValueError as err:
#     return err

import unittest
import main

class TestMain(unittest.TestCase):
  def setUp(self):
    print('About to test a function')

  def test_do_stuff(self):
    test_param= 10
    result = main.do_stuff(test_param)
    self.assertEqual(result, 15)

  def test_do_stuff2(self):
    test_param = 'asdaf'
    result = main.do_stuff(test_param)
    self.assertIsInstance(result, ValueError)

  def test_do_stuff3(self):
    test_param = None
    result = main.do_stuff(test_param)
    self.assertEqual(result, 'Please enter a number')

  def test_do_stuff4(self):
    test_param = ''
    result = main.do_stuff(test_param)
    self.assertEqual(result, 'Please enter a number')

  def tearDown(self):
      print('cleaning up')

if __name__ == '__main__':
  unittest.main()