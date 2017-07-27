#!/usr/bin/python

import sys

tsales = 0
past_cat = None

for line in sys.stdin:
	data_mapper = line.strip().split("\t")
	
	if len(data_mapper) != 2:
		continue
	present_cat, sales = data_mapper

	if past_cat and past_cat != present_cat:
		print past_cat, "\t", tsales
		past_cat = present_cat;
		tsales = 0

	past_cat = present_cat
	tsales += float(sales)

if past_cat != None:
	print past_cat,"\t", tsales

