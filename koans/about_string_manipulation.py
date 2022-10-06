#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutStringManipulation(Koan):

    def test_use_format_to_interpolate_variables(self):
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        # https://docs.python.org/3/tutorial/inputoutput.html
        # self.assertEqual(__, string)
        self.assertEqual("The values are one and 2", string)

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        # self.assertEqual(__, string)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string)

    def test_any_python_expression_may_be_interpolated(self):
        import math  # import a standard python module with math functions

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
                                                            decimal_places)
        # you can format using methods to get values or strings that will insert into the main string
        # self.assertEqual(__, string)
        self.assertEqual("The square root of 5 is 2.2361", string)

    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
        # self.assertEqual(__, string[7:10])
        self.assertEqual('let', string[7:10])

    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        # self.assertEqual(__, string[1])
        self.assertEqual('a', string[1])

    def test_single_characters_can_be_represented_by_integers(self):
        # use ord function to get a numerical value for each char in a string
        # self.assertEqual(__, ord('a'))
        # self.assertEqual(__, ord('b') == (ord('a') + 1))
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, ord('b') == (ord('a') + 1))

    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        # split string into list by default where spaces are but can specify by char
        # self.assertListEqual([__, __, __], words)
        self.assertListEqual(['Sausage', 'Egg', 'Cheese'], words)

    def test_strings_can_be_split_with_different_patterns(self):
        import re  # import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;')

        words = pattern.split(string)

        # self.assertListEqual([__, __, __, __], words)
        self.assertListEqual(['the', 'rain', 'in', 'spain'], words)

        # Pattern is a Python regular expression pattern which matches ',' or ';'

    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n'
        self.assertNotEqual('\n', string)
        # https://stackoverflow.com/questions/66857781/print-length-of-raw-string-value-of-an-list-of-strings
        # self.assertEqual(__, string)
        # self.assertEqual(__, len(string))
        self.assertEqual('\\n', string)
        self.assertEqual(2, len(string))

        # Useful in regular expressions, file paths, URLs, etc.

    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        # https://www.geeksforgeeks.org/python-string-join-method/
        # self.assertEqual(__, ' '.join(words))
        self.assertEqual('Now is the time', ' '.join(words))

    def test_strings_can_change_case(self):
        # https://www.geeksforgeeks.org/string-capitalize-python/
        # self.assertEqual(__, 'guido'.capitalize())
        # self.assertEqual(__, 'guido'.upper())
        # self.assertEqual(__, 'TimBot'.lower())
        # https://www.geeksforgeeks.org/title-in-python/
        # self.assertEqual(__, 'guido van rossum'.title())
        # https://www.geeksforgeeks.org/python-string-swapcase/
        # self.assertEqual(__, 'ToTaLlY aWeSoMe'.swapcase())
        self.assertEqual('Guido', 'guido'.capitalize())
        self.assertEqual('GUIDO', 'guido'.upper())
        self.assertEqual('timbot', 'TimBot'.lower())
        self.assertEqual('Guido Van Rossum', 'guido van rossum'.title())
        self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase())
