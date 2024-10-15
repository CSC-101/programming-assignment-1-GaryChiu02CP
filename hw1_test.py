import data
import hw1
import unittest

from data import Price


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input = "aloha"
        result = hw1.vowel_count(input)
        expected = 3
        self.assertEqual(expected, result)

    def test_vowel_count_2(self):
        input = "a smorgasbord"
        result = hw1.vowel_count(input)
        expected = 4
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists_1(self):
        input = [[1],[2,3],[4,5,6],[7,8,9],[10,11]]
        result = hw1.short_lists(input)
        expected = [[2,3],[10,11]]
        self.assertEqual(expected, result)

    def test_short_lists_2(self):
        input = [[2,1],[4,6],[4,3],[2,3,4]]
        result = hw1.short_lists(input)
        expected = [[2,1],[4,6],[4,3]]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs_1(self):
        input = [[1], [2, 3], [4, 5, 6], [7, 8, 9], [12, 11]]
        result = hw1.ascending_pairs(input)
        expected = [[1], [2, 3], [4, 5, 6], [7, 8, 9], [11, 12]]
        self.assertEqual(expected, result)

    def test_ascending_pairs_2(self):
        input = [[2, 1], [4, 6], [4, 3], [2, 3, 4]]
        result = hw1.ascending_pairs(input)
        expected = [[1, 2], [4, 6], [3, 4], [2, 3, 4]]
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices_1(self):
        cost1 = Price(3,35)
        cost2 = Price(10, 35)
        result = hw1.add_prices(cost1, cost2)
        expected = Price(13, 70)
        self.assertEqual(expected, result)

    def test_add_prices_2(self):
        cost1 = Price(5, 55)
        cost2 = Price(5, 969)
        result = hw1.add_prices(cost1, cost2)
        expected = Price(20, 24)
        self.assertEqual(expected, result)

    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
