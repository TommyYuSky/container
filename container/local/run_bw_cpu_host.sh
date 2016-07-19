#! /bin/bash
#for i in `seq 1 20`;
#do
#        python teststress_localclient.py 3 0 $i
#done

python stress_client.py 4 0 1 1000
python stress_client.py 4 0 1 2000
python stress_client.py 4 0 1 3000
python stress_client.py 4 0 1 4000
python stress_client.py 4 0 1 5000
python stress_client.py 4 0 1 6000
python stress_client.py 4 0 1 8000
python stress_client.py 4 0 1 10000
python stress_client.py 4 0 1 15000
python stress_client.py 4 0 1 20000
python stress_client.py 4 0 1 25000
python stress_client.py 4 0 1 30000
python stress_client.py 4 0 1 35000
python stress_client.py 4 0 1 40000
python stress_client.py 4 0 1 45000
python stress_client.py 4 0 1 50000
