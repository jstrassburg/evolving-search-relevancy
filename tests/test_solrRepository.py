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
from SolrRepository import SolrRepository


class TestSolrRepository(TestCase):
    def test_search(self):
        results = SolrRepository.search("crab shack", 10, 2)
        self.assertEqual(len(results), 1, "Expected one result")
        result = list(results)[0]
        self.assertEqual(result["name"], "Joe's Crab Shack")

    def test_search_zero_boost_name(self):
        results = SolrRepository.search("red", 0, 2)
        self.assertEqual(len(results), 1)
        result = list(results)[0]
        self.assertEqual(result["name"], "Joe's Crab Shack")

    def test_search_zero_boost_description(self):
        results = SolrRepository.search("red", 2, 0)
        self.assertEqual(len(results), 1)
        result = list(results)[0]
        self.assertEqual(result["name"], "Red Lobster")

    def test_interactive_queries(self):
        expected = ["red lobster", "crabs", "seafood", "lobster"]
        results = SolrRepository.interactive_queries()
        self.assertItemsEqual(results, expected)

    def test_total_matches(self):
        expected = 2
        actual = SolrRepository.total_matches("seafood")
        self.assertEqual(actual, expected)