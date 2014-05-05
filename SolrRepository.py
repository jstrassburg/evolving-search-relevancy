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
import solr
import sys


class SolrRepository:
    rows = sys.maxint
    solr_connection = solr.SolrConnection('http://localhost:8983/solr/restaurantsCollection')

    def __init__(self):
        pass

    @staticmethod
    def search(q, name_boost, description_boost):
        qf = "name^{0} description^{1}".format(name_boost, description_boost)
        return SolrRepository.solr_connection.query(q, rows=SolrRepository.rows, qf=qf, defType="dismax", q_alt="*:*")

    @staticmethod
    def interactive_queries():
        results = SolrRepository.solr_connection.query("*:*", rows=SolrRepository.rows, fl="searchTermInteractions")
        queries = set()
        for result in results:
            for term in result["searchTermInteractions"]:
                queries.add(term)
        return queries

    @staticmethod
    def total_matches(query):
        results = SolrRepository.solr_connection.query(
            "searchTermInteractions:{0}".format(query), rows=SolrRepository.rows)
        return results.numFound