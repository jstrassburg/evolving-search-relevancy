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
#   limitations under the License.
import random
from SearchParameter import SearchParameter
from SolrRepository import SolrRepository


class CandidateSolution:
    size = 8

    def __init__(self, bits=None):
        if bits is None:
            self.name_boost = SearchParameter()
            self.description_boost = SearchParameter()
        else:
            self.decode(bits)

    def decode(self, bits):
        """
        decodes a list of bits into this instance
        :param bits: A list of 0/1 to be sliced into the individual parameters
        """
        self.name_boost = SearchParameter(tuple(bits[0:4]))
        self.description_boost = SearchParameter(tuple(bits[4:8]))

    @staticmethod
    def evaluate(bits):
        """
        Calculates an average of the F-Measure for every query that has recorded interactions
        """
        candidate = CandidateSolution(bits)
        f_measures = []
        #for query in SolrRepository.interactive_queries():
        for query in ["red lobster"]:
            results = SolrRepository.search(query, candidate.name_boost.value, candidate.description_boost.value)
            precision = CandidateSolution.calculate_precision(query, results)
            recall = CandidateSolution.calculate_recall(query, results)
            f_measures.append(CandidateSolution.f_measure(precision, recall))
        return sum(f_measures) / len(f_measures),

    @staticmethod
    def f_measure(precision, recall):
        if (precision + recall) == 0:
            return 0
        return 2.0 * float(precision * recall) / float(precision + recall)

    @staticmethod
    def calculate_precision(query, results):
        total_results = float(results.numFound)
        return CandidateSolution.correct_matches(query, results) / total_results

    @staticmethod
    def calculate_recall(query, results):
        correct_matches = CandidateSolution.correct_matches(query, results)
        total_matches = float(SolrRepository.total_matches(query))
        missed_matches = total_matches - correct_matches
        return correct_matches / (correct_matches + missed_matches)

    @staticmethod
    def correct_matches(query, results):
        correct_matches = 0.
        for result in results:
            if query in result["searchTermInteractions"]:
                correct_matches += 1.
        return correct_matches