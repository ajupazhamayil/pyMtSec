#!/usr/bin/env python
import sys
for line in sys.stdin:
	str=line.rstrip().split(",")

	country=str[7]

	print(country +" 1")
