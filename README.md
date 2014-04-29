evolving-search-relevancy
=========================

Tuning Solr search engine parameters by treating them as an optimization problem and employing a genetic algorithm utilizing normalized discounted cumulative gain [NDCG] as a fitness measure.

Getting Started
===============
* Clone this repo
* Run the start_solr script to start Solr
* Run the following to import the dataset

        $ cd dataset
        $ curl 'http://localhost:8983/solr/productsCollection/update/json?commit=true' --data-binary @restaurants.json -H 'Content-type:application/json'

References
==========
* Distributed Evolutionary Algorithms in Python - [DEAP documentation](http://deap.gel.ulaval.ca/doc/default/index.html)
* Genetic Algorithm in Adaptive Web Search - [wordpress.com blog](http://mahbub.wordpress.com/2007/04/11/genetic-algorithm-in-adaptive-web-search/)
* Measuring Search Relevance - [eBay Tech Blog](http://www.ebaytechblog.com/2010/11/10/measuring-search-relevance/#.U16CjvldVJM)
* Discounted Cumulative Gain - [wikipedia](http://en.wikipedia.org/wiki/Discounted_cumulative_gain)
* Normalized Discounted Cumulative Gain - [kaggle](https://www.kaggle.com/wiki/NormalizedDiscountedCumulativeGain)
* Python Solr Module - [solrpy](https://code.google.com/p/solrpy/)
