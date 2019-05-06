#!/usr/bin/python3
import unittest

from main import Person, load_file
from alphabetizer import *

class TestAlphabetizer(unittest.TestCase):

    # def test_order_first_name(self):
    #     harry = Person('Harry', 'Potter', 'hpotter@hogwarts.edu')
    #     hermione = Person('Hermione', 'Granger', 'hgranger@hogwarts.edu')
    #     self.assertTrue(order_first_name(harry, hermione))
    #     self.assertFalse(order_first_name(hermione, harry))
    #
    # def test_order_first_name2(self):
    #     potter = Person('Albus', 'Potter', 'apotter@hogwarts.edu')
    #     dumbledore = Person('Albus', 'Dumbledore', 'adumbledore@hogwarts.edu')
    #     self.assertFalse(order_first_name(potter, dumbledore))
    #     self.assertTrue(order_first_name(dumbledore, potter))
    #
    # def test_order_last_name(self):
    #     harry = Person('Harry', 'Potter', 'hpotter@hogwarts.edu')
    #     hermione = Person('Hermione', 'Granger', 'hgranger@hogwarts.edu')
    #     self.assertFalse(order_last_name(harry, hermione))
    #     self.assertTrue(order_last_name(hermione, harry))
    #
    # def test_order_last_name2(self):
    #     fred = Person('Fred', 'Weasley', 'fweasley@hogwarts.edu')
    #     george = Person('George', 'Weasley', 'gweasley@hogwarts.edu')
    #     self.assertTrue(order_last_name(fred, george))
    #     self.assertFalse(order_last_name(george, fred))
    #
    # def test_is_alphabetized(self):
    #     member_list = load_file('gryffindor.txt')
    #     self.assertFalse(is_alphabetized(member_list, order_first_name))
    #     self.assertFalse(is_alphabetized(member_list, order_last_name))
    #     member_list = load_file('sorted_first_name.txt')
    #     self.assertTrue(is_alphabetized(member_list, order_first_name))
    #     member_list = load_file('sorted_last_name.txt')
    #     self.assertTrue(is_alphabetized(member_list, order_last_name))
    #
    # def test_alphabetize_by_first(self):
    #     member_list = load_file('gryffindor.txt')
    #     solution = load_file('sorted_first_name.txt')
    #     (sorted_list, cost) = alphabetize(member_list, order_first_name)
    #     self.assertEqual(sorted_list, solution)
    #
    # def test_alphabetize_by_last(self):
    #     member_list = load_file('gryffindor.txt')
    #     solution = load_file('sorted_last_name.txt')
    #     (sorted_list, cost) = alphabetize(member_list, order_last_name)
    #     self.assertEqual(sorted_list, solution)

    def number_test(self):
        data = [5, 3, 2, 6, 4, 9, 7, 1, 8]
        self.assertFalse(is_alphabetized(data, lambda a, b: a < b))
        self.assertFalse(is_alphabetized(data, lambda a, b: a > b))
        data = list(range(10))
        self.assertTrue(is_alphabetized(data, lambda a, b: a < b))
        self.assertFalse(is_alphabetized(data, lambda a, b: a > b))
        data = [1, 2, 3, 3, 4, 4, 5]
        self.assertTrue(is_alphabetized(data, lambda a, b: a < b))

if __name__ == '__main__':
    unittest.main()
