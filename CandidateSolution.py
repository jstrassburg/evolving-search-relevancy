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


class CandidateSolution:
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
    def random():
        """
        Returns a random list of bits in the correct length to be used a a candidate solution
        """
        name_boost = list(SearchParameter.random_bits())
        description_boost = list(SearchParameter.random_bits())
        return name_boost + description_boost