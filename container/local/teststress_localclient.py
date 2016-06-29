# !/usr/bin/python

# mesos
import argparse
import json
import time

# ssh
import subprocess
import sys

# string parse
import re

# MASTER="10.10.0.5"
# SLAVE1="10.10.0.5"
SLAVE2="127.0.0.1"
# SLAVE3="10.10.0.7"

# 1 for weave; 2 for docker; 3 for process
scene = 3

# ip range
ip_low = 0
ip_high = 4 # high + 1

debug = 0

# input args
for arg in sys.argv:
        if debug == 1:
                print arg

if len(sys.argv) > 1:
        scene = int(sys.argv[1])
        ip_low = int(sys.argv[2])
        ip_high = int(sys.argv[3])


result = []

ssh_dict={}
for i in range(ip_low,ip_high):
        if scene == 1:
                CMD="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0."+str(i)
        elif scene == 2:
                CMD="sudo docker run -t --rm networkstatic/iperf3 -c 172.17.0."+str(i)
	elif scene == 3:
                CMD="sudo iperf3 -c 127.0.0.1 -p 70"+str(i)

        #ssh = subprocess.Popen(["ssh","%s" % SLAVE2, CMD], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #print CMD+"\n"
        #ssh_dict["ssh"+str(i)] = subprocess.Popen(["ssh","%s" % SLAVE2, CMD], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ssh_dict["ssh"+str(i)] = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


for i in range(ip_low,ip_high):
        #result.append(ssh.stdout.strip().split('\n')[-1].split(','))   
        ssh = ssh_dict["ssh"+str(i)]
        if i==ip_low:
                #result.append(stdout.strip().split('\n')[-1].split(','))       
                result = ssh.stdout.readlines()
        else:
                result = result + ssh.stdout.readlines()
        if result == []:
                error = ssh.stderr.readlines()
                print >>sys.stderr, "ERROR: %s" % error

# elems stores all the words in a line
elems = []
bws = []
if result != []:
        #print result
        for line in result:
		if re.search("sender", line):
                        #print(line)
			elems = line.split()
			#print(elems[6])
			bwtemp = float(elems[6])
			if bwtemp > 100.0:
                                bwtemp = bwtemp/1000.0	
			bws.append(float(elems[6]))
	#print(bws)
	#print("\n")
	print(sum(bws))		
			

