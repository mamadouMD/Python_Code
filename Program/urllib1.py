''' Program wrote by Mamadou M Diallo 12/31/2015
	
	Read a file from a website
'''

import urllib

data = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in data:
	print line
