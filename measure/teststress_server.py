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
SLAVE2="10.10.0.6"
# SLAVE3="10.10.0.7"

# Control
# 1 for weave; 2 for docker; 3 for process;
scene = 3
# number of iperf3 servers
servernum = 20

# program 

# ssh
for i in range(servernum):
	if scene == 1:
		CMD="sudo docker run --net=weave -t --rm networkstatic/iperf3 -s"
	elif scene == 2:
		CMD="sudo docker run -t --rm networkstatic/iperf3 -s"
	elif scene == 3:
		CMD="sudo iperf3 -s -p 70"+str(i)
	print(CMD+"\n")
	ssh = subprocess.Popen(["ssh","%s" % SLAVE2, CMD], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	time.sleep(1);
	#result = ssh.stdout.readlines()
	#if result == []:
	#	error = ssh.stderr.readlines()
	#	print >>sys.stderr, "ERROR: %s" % error
	#else:
	#	print result

