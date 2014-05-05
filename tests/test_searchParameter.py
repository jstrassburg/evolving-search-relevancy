#   Copyright 2014 James Strassburg
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
from unittest import TestCase
from SearchParameter import SearchParameter


class TestSearchParameter(TestCase):
    allowed_values = [0, .2, .4, .6, .8, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    allowed_bits = [
        (0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1),
        (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 1, 0), (0, 1, 1, 1),
        (1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 1, 0), (1, 0, 1, 1),
        (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1),
    ]

    def test_default_constructor(self):
        actual = SearchParameter()
        self.assertIn(actual.value, TestSearchParameter.allowed_values)

    def test_constructor_with_decimal_value(self):
        expected = .4
        actual = SearchParameter((0, 0, 1, 0))
        self.assertEqual(actual.value, expected)

    def test_constructor_with_fibonacci_value(self):
        expected = 89
        actual = SearchParameter((1, 1, 1, 0))
        self.assertEqual(actual.value, expected)

    def test_random_value(self):
        actual = SearchParameter.random_value()
        self.assertIn(actual, TestSearchParameter.allowed_values)

    def test_random_bits(self):
        actual = SearchParameter.random_bits()
        self.assertIn(actual, TestSearchParameter.allowed_bits)