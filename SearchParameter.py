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


class SearchParameter:
    """
    Represents a numerical value that can be used with a search parameter.
    Examples: Boost values, slop values, min-should-match values, etc...
    """
    def __init__(self, bits=None):
        if bits is None:
            self.value = SearchParameter.random_value()
        else:
            self.value = SearchParameter.value_map[bits]

    @staticmethod
    def random_value():
        return random.choice(SearchParameter.value_map.values())

    @staticmethod
    def random_bits():
        return random.choice(SearchParameter.value_map.keys())

    # For parameter values, I've chosen 0.0, 0.2, 0.4, 0.8 and the first few numbers
    # from the Fibonacci sequence which encode nicely into 4 bits of data
    value_map = {
        (0, 0, 0, 0): 0,
        (0, 0, 0, 1): 0.2,
        (0, 0, 1, 0): 0.4,
        (0, 0, 1, 1): 0.6,
        (0, 1, 0, 0): 0.8,
        (0, 1, 0, 1): 1,
        (0, 1, 1, 0): 2,
        (0, 1, 1, 1): 3,
        (1, 0, 0, 0): 5,
        (1, 0, 0, 1): 8,
        (1, 0, 1, 0): 13,
        (1, 0, 1, 1): 21,
        (1, 1, 0, 0): 34,
        (1, 1, 0, 1): 55,
        (1, 1, 1, 0): 89,
        (1, 1, 1, 1): 144,
    }