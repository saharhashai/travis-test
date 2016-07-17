import unittest


class TravisTest(unittest.TestCase):
    def test_fail(self):
        self.assertEqual(1, 0)

    def test_success(self):
        self.assertEqual(1, 1)


suite = unittest.TestLoader().loadTestsFromTestCase(TravisTest)
unittest.TextTestRunner(verbosity=2).run(suite)