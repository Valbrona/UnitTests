import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self): # this is used to interfere between each tests
        print("about to test a function")

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "hjdgasjd"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter number")

    def test_do_stuff4(self):
        test_param = ""
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter number")

    def test_do_stuff5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result,"no zeroes allowed")

    def tearDown(self): # it is normally used to test Databases (for longer codes)
        print("cleaning up")

if __name__ == "__main__":  # by adding this lines, we are able to run multiple times in one go, by typing python3 -m unittest in Terminal (by adding the -v after unittest, it will give an overview of all the tests, that have run and their statuses)
    unittest.main()
