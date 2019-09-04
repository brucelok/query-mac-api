#!/usr/bin/python
import unittest
from macapi import *

class SimpleTest(unittest.TestCase):

    def test_default(self):
        self.assertTrue(True)

    def test_error_404(self):
        result = handle_404_error('404')
        self.assertEqual(result, 'not found')

if __name__ == '__main__':
    unittest.main()
