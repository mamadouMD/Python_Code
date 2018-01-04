import urllib
import xml.etree.ElementTree as ET


address = raw_input('Enter Xml Url: ')

print 'Retrieving', address 

#open the url/ address
uh = urllib.urlopen(address)
# Read the web page
data = uh.read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)

# find/parsing until the "comment" sub_level inside the xml file
results = tree.findall('comments/comment')

sum = 0 
count = 0
# loop inside the parsed xml to find the count tags
for items in results:
	#print "count", items.find('count').text
	value = items.find('count').text
	sum = sum + int(value)
	count += 1
	
	#print "name", items.find('name').text


print "Count: ", count
print "Sum: ", sum