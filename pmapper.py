#!/usr/bin/python

import sys

for line in sys.stdin:
	sale = line.strip().split(",")

	if len(sale) == 5:
		TransactionId,name,category,state,amount= sale

		print state,"\t",amount
