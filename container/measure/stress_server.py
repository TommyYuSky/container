# !/usr/bin/python

# mesos
import argparse
import json
import time

# ssh
import subprocess
import sys

# Constant
# MASTER="10.10.0.5"
# SLAVE1="10.10.0.5"
SLAVE2="10.10.0.10"
# SLAVE3="10.10.0.7"

# Control
# 1 for same VM; 2 for different VM;
samevm = 1
# 1 for weave; 2 for docker; 3 for process;
scene = 1
# number of iperf3 servers
servernum = 1

ssh_dict={}

# input args
for arg in sys.argv:
	print arg 

if len(sys.argv) > 1:
	samevm = int(sys.argv[1])
	scene = int(sys.argv[2])
	servernum = int(sys.argv[3])

# ssh
for i in range(servernum):
	if samevm == 1:	
		if scene == 1:
			CMD="sudo docker run --net=weave -t --rm networkstatic/iperf3 -s"
		elif scene == 2:
			CMD="sudo docker run -t --rm networkstatic/iperf3 -s"
		elif scene == 3:
			CMD="sudo iperf3 -s 127.0.0.1 -p 70"+str(i)
	elif samevm == 2:
		if scene == 1:
			CMD="sudo docker run --net=weave -t --rm networkstatic/iperf3 -s"
		elif scene == 2:
			CMD="sudo docker run -t --rm networkstatic/iperf3 -s"
		elif scene == 3:
			CMD="sudo iperf3 -s -p 70"+str(i)
			
	print(CMD+"\n")
	ssh_dict["ssh"+str(i)] = subprocess.Popen(["ssh","%s" % SLAVE2, CMD], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	time.sleep(0.5)
	#result = ssh.stdout.readlines()
	#if result == []:
	#	error = ssh.stderr.readlines()
	#	print >>sys.stderr, "ERROR: %s" % error
	#else:
	#	print result

for i in range(servernum):
        ssh = ssh_dict["ssh"+str(i)]
	result = ssh.stdout.readlines()
	if result == []:
		error = ssh.stderr.readlines()
		print >>sys.stderr, "ERROR: %s" % error
	else:
		print result
