import unittest
import sys

class TravisTest(unittest.TestCase):
    def test_fail(self):
        self.assertEqual(1, 0)

    def test_success(self):
        self.assertEqual(1, 1)


suite = unittest.TestLoader().loadTestsFromTestCase(TravisTest)
ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
sys.exit(ret)