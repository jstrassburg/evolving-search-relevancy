evolving-search-relevancy
=========================

Tuning Solr search engine parameters by treating them as an optimization problem and employing a genetic algorithm utilizing normalized discounted cumulative gain [NDCG] as a fitness measure.

Getting Started
===============
* Clone this repo
* Run the start_solr script to start Solr
* Run solrimport.py to import the dataset to your Solr instance

References
==========
* Data set - [Abbott Vascular Product Inventory](http://www.abbottvascular.com/us/product-catalogs.html)
* Distributed Evolutionary Algorithms in Python - [DEAP documentation](http://deap.gel.ulaval.ca/doc/default/index.html)
* Genetic Algorithm in Adaptive Web Search - [wordpress.com blog](http://mahbub.wordpress.com/2007/04/11/genetic-algorithm-in-adaptive-web-search/)
* Measuring Search Relevance - [eBay Tech Blog](http://www.ebaytechblog.com/2010/11/10/measuring-search-relevance/#.U16CjvldVJM)
* Discounted Cumulative Gain - [wikipedia](http://en.wikipedia.org/wiki/Discounted_cumulative_gain)
* Normalized Discounted Cumulative Gain - [kaggle](https://www.kaggle.com/wiki/NormalizedDiscountedCumulativeGain)
* Python Solr Module - [solrpy](https://code.google.com/p/solrpy/)
