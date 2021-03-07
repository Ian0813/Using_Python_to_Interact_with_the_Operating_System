#!/usr/bin/python3



import unittest
from juypter_LetterCompiler import LetterCompiler

class TestCompiler2(unittest.TestCase):
    
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE

unittest.main(argv = ['first-arg-is-ignored'], exit = False)

