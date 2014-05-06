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
import math
from unittest import TestCase
from CandidateSolution import CandidateSolution
from SolrRepository import SolrRepository


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

    def test_f_measure_zeros(self):
        actual = CandidateSolution.f_measure(0, 0)
        self.assertEqual(actual, 0)

    def test_f_measure(self):
        precision = 10
        recall = 20
        expected = 2. * 200. / 30.
        actual = CandidateSolution.f_measure(precision, recall)
        self.assertEqual(actual, expected)

    def test_correct_matches(self):
        query = "red lobster"
        results = SolrRepository.search(query, 1, 1)
        actual = CandidateSolution.correct_matches(query, results)
        expected = 1
        self.assertEqual(actual, expected)

    def test_discounted_correct_matches(self):
        query = "red lobster"
        results = SolrRepository.search(query, 1, 1)
        actual = CandidateSolution.discounted_correct_matches(query, results)
        expected = 1. / math.log(3)
        self.assertEqual(actual, expected)