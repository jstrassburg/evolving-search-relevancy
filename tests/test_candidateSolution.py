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
from CandidateSolution import CandidateSolution


class TestCandidateSolution(TestCase):
    allowed_values = [0, .2, .4, .6, .8, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

    def test_default_constructor(self):
        actual = CandidateSolution()
        self.assertIn(actual.name_boost.value, TestCandidateSolution.allowed_values)

    def test_constructor_with_bits(self):
        actual = CandidateSolution([1, 1, 0, 0, 0, 0, 0, 1])
        expected_name_boost = 34
        expected_description_boost = .2
        self.assertEqual(actual.name_boost.value, expected_name_boost, "Name boost was incorrect")
        self.assertEqual(actual.description_boost.value, expected_description_boost, "Description boost was incorrect")