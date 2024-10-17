import data
import hw1
import unittest

from data import Price, Point, Rectangle, Circle, Book, Employee


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
    def test_rectangle_area_1(self):
        x = Rectangle(Point(0, 0), Point(5, 10))
        input = x
        result = hw1.rectangle_area(input)
        expected = 50
        self.assertEqual(expected, result)

    def test_rectangle_area_2(self):
        x = Rectangle(Point(-5, -5), Point(5, 5))
        input = x
        result = hw1.rectangle_area(input)
        expected = 100
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author_1(self):
        name = "James"
        bk1 = Book(["James"], "Calculus 8th Edition 2016")
        bk2 = Book(["Rebecca"], "Health")
        books = [bk1, bk2]
        result = hw1.books_by_author(name, books)
        expected = [bk1]
        self.assertEqual(expected, result)

    def test_books_by_author_2(self):
        name = "qntm"
        bk1 = Book(["qntm"], "Ed")
        bk2 = Book(["qntm", "Victor Wu"], "Lena")
        bk3 = Book(["Scott"], "Unsong")
        books = [bk1, bk2, bk3]
        result = hw1.books_by_author(name, books)
        expected = [bk1, bk2]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound_1(self):
        p1 = Point(0, 0)
        p2 = Point(6, 8)
        rect = Rectangle(p1, p2)
        result = hw1.circle_bound(rect)
        expected = Circle(Point(3, 4), 5)
        self.assertEqual(expected, result)

    def test_circle_bound_2(self):
        p1 = Point(-10, -10)
        p2 = Point(-6, -7)
        rect = Rectangle(p1, p2)
        result = hw1.circle_bound(rect)
        expected = Circle(Point(2, 1.5), 2.5)
        self.assertEqual(expected, result)

    # Part 8
    def test_below_pay_average_1(self):
        e1 = Employee("Lucas" , 17)
        e2 = Employee("Russel", 18)
        e3 = Employee("Bradley", 18)
        e4 = Employee("Caleb", 16)
        e5 = Employee("Bobby", 20)
        e6 = Employee("Roy", 18)
        e7 = Employee("Liam", 17)
        e8 = Employee("Vincent", 19)
        e9 = Employee("Mason", 16)
        input = [e1,e2,e3,e4,e5,e6,e7,e8,e9]
        result = hw1.below_pay_average(input)
        expected = [e1,e4,e7,e9]
        self.assertEqual(expected, result)

    def test_below_pay_average_2(self):
        e1 = Employee("Randy", 16)
        e2 = Employee("Wayne", 20)
        e3 = Employee("Albert", 17)
        e4 = Employee("Willie", 20)
        e5 = Employee("Elijah", 20)
        e6 = Employee("Juan", 19)
        e7 = Employee("Alan", 18)
        e8 = Employee("Joe", 20)
        e9 = Employee("Billy", 16)
        input = [e1, e2, e3, e4, e5, e6, e7, e8, e9]
        result = hw1.below_pay_average(input)
        expected = [e1,e3,e7,e9]
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()