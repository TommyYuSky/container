#! /bin/bash
for i in `seq 2 21`;
do
	# echo $i
	# Process
	# python stress_client.py 1 3 2 0 1 1000
	python stress_client.py 1 1 2 1 $i 1000
	# Docker
	# python stress_client.py 1 2 2 2 3 1000
	# Weave
	#python stress_client.py 1 1 2 22 23 1000
done
