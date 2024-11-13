# tests/test_anagram_checker.py

import unittest
from anagram_checker import are_anagrams

class TestAnagramChecker(unittest.TestCase):
    def test_anagrams(self):
        self.assertTrue(are_anagrams("star", "rats"))
        self.assertTrue(are_anagrams("I am lord voldemort", "Tom Marvolo Riddle"))
        self.assertFalse(are_anagrams("hello", "world"))
        self.assertTrue(are_anagrams("Neil A.", "alien"))

if __name__ == "__main__":
    unittest.main()
