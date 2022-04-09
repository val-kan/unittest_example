"""
Example of basic tests with unittest.
1. Class name starts with "Test"
2. Each test method starts with "test_"
3. main calls unittest.main()
"""
import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_lower(self):
        self.assertEqual('FOO'.lower(), 'foo')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    @unittest.skip('demonstrating skipping test')
    def test_nothing(self):
        self.fail('Should never happen')


if __name__ == '__main__':
    unittest.main()
