import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print("testing function")

    def test_do_stuff(self):
        test_num = 10
        result = main.do_stuff(test_num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_num = "klbdheueswbno"
        result = main.do_stuff(test_num)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_num = None
        result = main.do_stuff(test_num)
        self.assertEqual(result, "please enter number!")

    def test_do_stuff4(self):
        test_num = ""
        result = main.do_stuff(test_num)
        self.assertEqual(result, "please enter number!")

    def test_do_stuff5(self):
        test_num = 0
        result = main.do_stuff(test_num)
        self.assertEqual(result, 5)

    def tearDown(self):
        print("cleaning up")


if __name__ == "__main__":
    unittest.main()
