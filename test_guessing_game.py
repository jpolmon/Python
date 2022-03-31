import unittest
import guessing_game

class TestGame(unittest.TestCase):
  def setUp(self):
    print('About to test a function')

  def test_guess(self):
    test_param = 11
    result = guessing_game.guessing_game(test_param, 10)
    self.assertEqual(result, 'Hey, it\'s supposed to be 1~10')

  def tearDown(self):
      print('cleaning up')

if __name__ == '__main__':
  unittest.main()