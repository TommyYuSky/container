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
SLAVE2="10.10.0.10"
# SLAVE3="10.10.0.7"

# debug
debug = 0

# zero copy mod: use zero copy system call - sendfile()
# 1: use zero copy; 2 no zero copy
# 3: limited bandwidth
zerocopy = 3

# 1 for same VM; 2 for different VM;
samevm = 1
# 1 for weave; 2 for docker; 3 for process
scene = 2

# records
cpu_all = []
mem_all = []
bw_all = []

# ip range
ip_low = 2
ip_high = 11 # high + 1

# input args
for arg in sys.argv:
	if debug == 1:
        	print arg

if len(sys.argv) > 1:
        samevm = int(sys.argv[1])
        scene = int(sys.argv[2])
	zerocopy = int(sys.argv[3])
        ip_low = int(sys.argv[4])
        ip_high = int(sys.argv[5])
	bw_lim = int(sys.argv[6]) 
 
result = []
ssh_dict={}
CMD = ""
for i in range(ip_low,ip_high):
	if samevm == 1:
		if scene == 1:				
			if zerocopy == 1:
				CMD="sudo docker run --net=weave -t --rm networkstatic/iperf3 -Z -c 10.32.0."+str(i)
			elif zerocopy == 2:
				CMD="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.32.0."+str(i)
			elif zerocopy == 3:
				CMD="sudo docker run --net=weave -t --rm networkstatic/iperf3 -b "+str(bw_lim)+"M -c 10.32.0."+str(i)
			elif zerocopy == 4:
				CMD="sudo docker run --net=weave -t --rm networkstatic/iperf3 -u -b "+str(bw_lim)+"M -c 10.32.0."+str(i)
		elif scene == 2:
			if zerocopy == 1:
				CMD="sudo docker run -t --rm networkstatic/iperf3 -Z -c 172.17.0."+str(i)
			elif zerocopy == 2:
				CMD="sudo docker run -t --rm networkstatic/iperf3 -c 172.17.0."+str(i)
		elif scene == 3:
			if zerocopy == 1:
				CMD="sudo iperf3 -Z -c 127.0.0.1 -p 70"+str(i)
			elif zerocopy == 2:
				CMD="sudo iperf3 -c 127.0.0.1 -p 70"+str(i)
	elif samevm == 2:
		if scene == 1:				
			CMD="sudo docker run --net=weave -t --rm networkstatic/iperf3 -c 10.32.0."+str(i)
		elif scene == 2:
			CMD="sudo docker run -t --rm networkstatic/iperf3 -c 10.10.0.10 -p 70"+str(i)
		elif scene == 3:
			CMD="sudo iperf3 -c 10.10.0.6 -p 70"+str(i)
	
	
	if debug == 1:
		print CMD+"\n"
	ssh_dict["ssh"+str(i)] = subprocess.Popen(["ssh","%s" % SLAVE2, CMD], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
# add subprocess to measure CPU & Memory
# TOP="for i in {1..10}; do top -bn 2 -d 0.01 | grep -A1 '^%Cpu' | tail -n 2 | tr -d \"\n\" | tr -d \"ni,\"| gawk '{print $2+$4+$6, $21}'; sleep 1; done"
#TOP="for i in {1..20}; do top -bn 2 -d 0.01 | grep 'iperf' | gawk '{ sum1+=$9; sum2+=$10} END {print sum1, sum2}'; sleep 1; done"
#TOP="for i in {1..20}; do top -c -bn 2 -d 0.01 | grep 'iperf' | gawk '{ sum1+=$9; sum2+=$10} END {print sum1, sum2}'; sleep 1; done"

#TOP = "for i in {1..20}; do top -c -bn 2 -d 0.01 | grep 'iperf3 -s\|iperf3 -b' | gawk '{ if( $13 == \"-s\") {sum1+=$9; sum2+=$10} else if($13 == \"-b\") {sum3+=$9; sum4+=$10} } END {print sum1, sum2, sum3, sum4}'; sleep 1; done"
TOP = "for i in {1..20}; do top -c -bn 2 -d 0.01 | grep 'iperf3 -s\|iperf3 -u' | gawk '{ if( $13 == \"-s\") {sum1+=$9; sum2+=$10} else if($13 == \"-u\") {sum3+=$9; sum4+=$10} } END {print sum1, sum2, sum3, sum4}'; sleep 1; done"
if debug == 1:
	print TOP+"\n"
top1 = subprocess.Popen(["ssh","%s" % SLAVE2, TOP], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# process top result
cpu_sum = 0
cpu_v = []
mem_sum = 0
mem_v = []
cpu_sum2 = 0
cpu2_v =[]
mem_sum2 = 0
mem2_v = []
top_result = top1.stdout.readlines()
for line in top_result:
	elems = line.split()
	cpu_sum = cpu_sum + float(elems[0])
	mem_sum = mem_sum + float(elems[1])
	cpu_v.append(float(elems[0]))
	mem_v.append(float(elems[1]))
	if len(elems) > 2:
		cpu_sum2 = cpu_sum2 + float(elems[2])
		cpu2_v.append(float(elems[2]))
	if len(elems) > 3:
		mem_sum2 = mem_sum2 + float(elems[3])
		mem2_v.append(float(elems[3]))
cpu_avg = cpu_sum/len(top_result)
mem_avg = mem_sum/len(top_result)
cpu_avg2 = cpu_sum2/len(top_result)
mem_avg2 = mem_sum2/len(top_result)
#cpu_avg = max(cpu_v)
#mem_avg = max(mem_v)
#cpu_avg2 = max(cpu2_v)
#mem_avg2 = max(mem2_v)
if debug == 1:
	print "CPU: "+str(cpu_avg)+"\n"
	print "Mem: "+str(mem_avg)+"\n"	

# process client output
for i in range(ip_low,ip_high):
	ssh = ssh_dict["ssh"+str(i)]
	if i==ip_low:
		result = ssh.stdout.readlines()
	else:
		result = result + ssh.stdout.readlines()
	if result == []:
		error = ssh.stderr.readlines()
		if debug == 1: 
			print >>sys.stderr, "ERROR: %s" % error

# elems stores all the words in a line
elems = []
bws = []
bwtemp = 0
if result != []:
	#print result
	for line in result:
		if debug == 1:
			print(line)
		# if re.search("sender", line):
		if re.search("%", line):
			if debug == 1:
				print(line)
			elems = line.split()
                        if debug == 1:
				print(elems[6],elems[7])
			bwtemp = float(elems[6])
			if bwtemp > 100.0:
				bwtemp = bwtemp/1000.0
                        #bws.append(float(elems[6]))
                        bws.append(bwtemp)
	if debug == 1:
		print(len(bws))
        	print("\n") 
		print(bws)
        	print("\n")
        	print(sum(bws))

print(str(cpu_avg)+" "+str(mem_avg)+" "+str(cpu_avg2)+" "+str(mem_avg2)+" "+str(sum(bws)))
#print(str(sum(bws)))
# print("\n")
