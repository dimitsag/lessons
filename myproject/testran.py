import unittest
import randomnum

class TestMain(unittest.TestCase):
	def test_randomnum(self):
		result = randomnum.guess_game(5, 5)
		self.assertTrue(result)

	def test_randomnum_wrong_guess(self):
		result = randomnum.guess_game(5, 0)
		self.assertFalse(result)

	def test_randomnum_over_10(self):
		result = randomnum.guess_game(5, 20)
		self.assertFalse(result)

	def test_randomnum_string(self):
		result = randomnum.guess_game(5, "ghs")
		self.assertFalse(result)

	def test_randomnum_list(self):
		result = randomnum.guess_game(5, [1,2,3])
		self.assertFalse(result)


if __name__ == "__main__":
	unittest.main()