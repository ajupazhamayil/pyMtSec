#!/usr/bin/env python
import sys
prev=None
total=0
print("Output")
for line in sys.stdin:
	country,count=line.rstrip().split(" ")
	count=map(int,count)
	if prev and country==prev:
		total+=1
		prev=country
			
	elif prev==None:

		total+=1
		prev=country
	else:
		print(prev+" "+str(total))
		total=1
		prev=country
if prev:
	print(prev+" "+str(total))
	
		
		
	
