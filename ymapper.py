#!/usr/bin/python

import sys

for line in sys.stdin:
	data_mapped = line.strip().split(",")
	if len(data_mapped) == 5:
		TransactionId,name,category,state,amount = data_mapped
		print state,"\t",category,"\t",amount

