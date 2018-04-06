# Cloud-Assignment-4

Hadoop MapReduce CSV Analysis

The assignment reads the csv data file from the path /data/nyc/nyc-traffic.csv

The files mapper.py and reducer.py are cloned into Hadoop from GitHub using the below command

$ git clone https://github.uc.edu/madhyasa/Cloud-Assignment-4.git

To run the mapper.py and reducer.py scripts over the nyc-traffic.csv, use the below command

$ hadoop fs -cat /data/nyc/nyc-traffic.csv | python mapper.py | sort | python reducer.py

To run the MapReduce on hadoop cluster using Hadoop jar streaming, use the below command

$ hadoop jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.3.0-235.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /data/nyc/nyc-traffic.csv -output outfile

To check the results of the output file, use the below command

$ hadoop fs -cat /user/madhyasa/outfile/*
