#!/home/ajupazhamayil/venvPython/bin/python
import sys


for ip in sys.stdin:

 la = ip.rstrip().split(',')
 print(la[7]+" 1")
