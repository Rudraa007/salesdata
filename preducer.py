#!/usr/bin/python

import sys

tsales = 0
old_state = None

for line in sys.stdin:
	state,sales  = line.strip().split("\t",1)
	sales = float(sales)
	if old_state == state:
		tsales += sales

	else:
		if old_state != None:
			print "%s\t%s"% (old_state,tsales)

		old_state = state
		tsales = sales

if old_state:
	print "%s\t%s"% (old_state,tsales)

