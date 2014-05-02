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


class SearchGeneticAlgorithm:
    def __init__(self):
        # For boost values, I've chosen 0.0,0.2,0.4,0.8 and the first few numbers
        # from the Fibonacci sequence which encode nicely into 4 bits of data
        self.boost_map = {
            0.0: 0b0000, 0.2: 0b0001, 0.4: 0b0010, 0.6: 0b0011, 0.8: 0b0100, 1: 0b0101,
            2: 0b0110, 3: 0b0111, 5: 0b1000, 8: 0b1001, 13: 0b1010, 21: 0b1011,
            34: 0b1100, 55: 0b1101, 89: 0b1110, 144: 0b1111
        }
        self.encoded_boost_map = dict((v, k) for k, v in self.boost_map.iteritems())

    def random_boost(self):
        """
        Return a random encoded boost value
        """
        return random.choice(self.boost_map.values())

    def encode_boost(self, boost):
        """
        Encodes a boost value to its 4-bit binary equivalent
        """
        return self.boost_map[boost]

    def decode_boost(self, encoded_boost):
        """
        Decodes an boost value from its 4-bit binary equivalent
        """
        return self.encoded_boost_map[encoded_boost]