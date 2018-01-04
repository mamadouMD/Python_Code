'''

'''
# Program wrote by Mamadou M Diallo 01/06/2016

import json 
import urllib

url = raw_input("Entet the Url ==> ")

print 'Retrieving', url

u_url = urllib.urlopen(url)
data = u_url.read()

print 'Retrieved',len(data),'characters'

inf = json.loads(data)
#print inf['comments']

sum = 0
count = 0
for items in inf['comments']:
	#print 'value', items["count"]
	sum = sum + int(items["count"])
	count += 1
	
print 'count: ', count
print 'sum: ', sum

