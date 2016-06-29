#! /bin/bash
for i in `seq 1 20`;
do
        python teststress_localclient.py 3 0 $i
done
