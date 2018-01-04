''' 	
Actual problem: Start at: https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Romanie.html 
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times.
The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: A
'''

# Program wrote by Mamadou M Diallo 12/31/2015

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

#ask for count 
count = input("Enter count: ")

# ask the position
pos = input('Enter position: ')

for i in range(count):

	html = urllib.urlopen(url).read()

	#plug the htmal page into a beautifulsoup program 
	soup = BeautifulSoup(html)

	#retrive a list of link tags
	tags = soup('a')

	lo = 0

	for tag in tags:
		# let look the links from postion to 7 places futher
		lo = lo + 1
		if lo == pos:
			print tag.get('href', None)
			url = tag.get('href', None)
		
		else:
			continue
	
	
