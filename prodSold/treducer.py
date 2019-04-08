#!/home/ajupazhamayil/venvPython/bin/python
import sys

prev = None
total=0
for line in sys.stdin:
    country, count = line.rstrip().split(" ")
    count=int(count)
    if prev and country==prev:
        total=total+1
        continue
    elif prev==None:
        total=1
        prev=country
    else:
        print(prev+" "+str(total))
        prev=country
        total=1

if prev:
    print(country+" "+str(total))


