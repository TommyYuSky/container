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
SLAVE2="10.10.0.7"
SLAVE3="10.10.0.7"
# CMD1="uname -a"
CMD2="sudo docker run --net=weave -t --rm --name=iperf3-server2 networkstatic/iperf3 -s"

CMD3="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.1"
CMD4="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.6"
CMD5="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.7"
CMD6="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.8"
CMD7="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.9"
CMD8="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.10"
CMD9="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.11"
CMD10="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.12"
CMD11="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.13"
CMD12="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.14"


CMD13="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.15"
CMD14="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.16"
CMD15="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.17"
CMD16="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.18"
CMD17="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.19"
CMD18="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.20"
CMD19="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.21"
CMD20="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.22"
CMD21="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.23"
CMD22="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.40.0.24"
#ssh2 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD2], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# wait for server to setup
#time.sleep(5)

ssh3 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD3], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ssh4 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD4], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ssh5 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD5], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ssh6 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD6], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ssh7 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD7], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

ssh8 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD8], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ssh9 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD9], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ssh10 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD10], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ssh11 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD11], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ssh12 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD12], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#ssh13 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD13], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#ssh14 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD14], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#ssh15 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD15], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#ssh16 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD16], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#ssh17 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD17], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#ssh18 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD18], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#ssh19 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD19], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#ssh20 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD20], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#ssh21 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD11], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#ssh22 = subprocess.Popen(["ssh","%s" % SLAVE2, CMD12], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#result = ssh2.stdout.readlines()
#if result == []:
#	error = ssh2.stderr.readlines()
#	print >>sys.stderr, "ERROR: %s" % error
#else:
#	print result

result = ssh3.stdout.readlines()
result = result+ssh4.stdout.readlines()
result = result+ssh5.stdout.readlines()
result = result+ssh6.stdout.readlines()
result = result+ssh7.stdout.readlines()

result = result+ssh8.stdout.readlines()
result = result+ssh9.stdout.readlines()
result = result+ssh10.stdout.readlines()
result = result+ssh11.stdout.readlines()
result = result+ssh12.stdout.readlines()

#result = result+ssh13.stdout.readlines()
#result = result+ssh14.stdout.readlines()
#result = result+ssh15.stdout.readlines()
#result = result+ssh16.stdout.readlines()
#result = result+ssh17.stdout.readlines()

#result = result+ssh18.stdout.readlines()
#result = result+ssh19.stdout.readlines()
#result = result+ssh20.stdout.readlines()
#result = result+ssh21.stdout.readlines()
#result = result+ssh22.stdout.readlines()
#result = result+ssh23.stdout.readlines()
if result == []:
	error = ssh3.stderr.readlines()
	print >>sys.stderr, "ERROR: %s" % error
else:
	print result
