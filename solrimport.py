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
import uuid


def main():
    """
    Imports the dataset into Solr
    """
    connection = solr.SolrConnection('http://localhost:8983/solr/productsCollection')
    connection.delete_query("*:*")

    with open("dataset/US_PRODUCT_CATALOG.csv", "r") as data:
        for line in data:
            writetosolr(connection, line)

    connection.commit()


def writetosolr(connection, line):
    data = line.split(',')
    businessunit = data[0]
    division = data[1]
    family = data[2]
    product = data[3]
    productdescription = data[4]
    barcode = data[7].rstrip()

    if businessunit != "Business Unit":
        connection.add(id=str(uuid.uuid1().hex), businessunit=businessunit, division=division, family=family,
                       product=product, productdescription=productdescription, barcode=barcode.strip())

if __name__ == "__main__":
    main()
