#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) == 5:
       TranscationId,name,category,state,amount = data
       print"{0}\t{1}".format(category, amount)

