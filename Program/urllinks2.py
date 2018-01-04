import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

sum = 0
count = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag and store the value into num
    num = tag.contents[0]
    sum = sum + int(num)
    #count the number of value
    count += 1
#print the sum and the number of count
print 'Sum: ',sum
print 'Count: ', count