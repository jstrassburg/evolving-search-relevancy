#!/bin/bash
cd dataset
curl 'http://localhost:8983/solr/restaurantsCollection/update/json?commit=true' --data-binary @restaurants.json -H 'Content-type:application/json'
cd ..
