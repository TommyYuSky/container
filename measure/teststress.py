# !/usr/bin/python

# mesos
import argparse
import json
import time

# ssh
import subprocess
import sys

# MASTER="10.10.0.5"
# SLAVE1="10.10.0.5"
SLAVE2="10.10.0.6"
SLAVE3="10.10.0.7"
# CMD1="uname -a"
CMD2="sudo docker run --net=weave -t --rm --name=iperf3-server2 networkstatic/iperf3 -s"

CMD3="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.1"

ssh2 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD2], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# wait for server to setup
time.sleep(5)

ssh3 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD3], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#result = ssh2.stdout.readlines()
#if result == []:
#	error = ssh2.stderr.readlines()
#	print >>sys.stderr, "ERROR: %s" % error
#else:
#	print result

result = ssh3.stdout.readlines()
if result == []:
	error = ssh3.stderr.readlines()
	print >>sys.stderr, "ERROR: %s" % error
else:
	print result
