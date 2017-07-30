#!/usr/bin/python

import sys

total_sales = 0
past_cat = None
past_state = None

for line in sys.stdin:
	state,category,sales = line.strip().split("\t")
	sales = float(sales)
	if past_cat == category and past_state == state:
		total_sales += sales 
	else:
		if past_cat != None and past_state != None:
			print past_state,"\t",past_cat,"\t",sales
		past_state = state
		past_cat = category
		total_sales = sales

if past_cat and past_state:
	print past_state,"\t",past_cat,"\t",total_sales

