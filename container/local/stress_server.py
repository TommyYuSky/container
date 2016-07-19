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

# Control
# 1 for weave; 2 for docker; 3 for process;
scene = 1
# number of iperf3 servers
servernum = 1

SLAVE2="127.0.0.1"
# ssh
for i in range(servernum):
        if scene == 1:
                CMD="sudo docker run --net=weave -t --rm networkstatic/iperf3 -s"
        elif scene == 2:
                CMD="sudo docker run -t --rm networkstatic/iperf3 -s"
        elif scene == 3:
                CMD="sudo iperf3 -s -p 70"+str(i)
        print(CMD+"\n")
        # ssh = subprocess.Popen(["ssh","%s" % SLAVE2, CMD], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ssh = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1);
