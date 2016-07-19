#! /bin/bash
#for i in `seq 1 20`;
#do
#        python teststress_localclient.py 3 0 $i
#done

python stress_client.py 1 1 2 1000
python stress_client.py 1 1 2 2000
python stress_client.py 1 1 2 3000
python stress_client.py 1 1 2 4000
python stress_client.py 1 1 2 5000
python stress_client.py 1 1 2 6000
python stress_client.py 1 1 2 8000
python stress_client.py 1 1 2 10000
python stress_client.py 1 1 2 15000
python stress_client.py 1 1 2 20000
python stress_client.py 1 1 2 25000
python stress_client.py 1 1 2 30000
python stress_client.py 1 1 2 35000
python stress_client.py 1 1 2 40000
python stress_client.py 1 1 2 45000
python stress_client.py 1 1 2 50000
