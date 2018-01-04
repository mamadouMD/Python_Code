# Program wrote by Mamadou Fri 12/29/2015
import re

file= raw_input('Enter the file name: ')
dat= open(file, 'r')

num=0
count = 0

for lines in dat:
	line = lines.strip() # take out the extra white space
	
	# look for numeric value and store it into a list y
	y= re.findall('[0-9]+', line) 
	
	for i in y:
		num = num + int(i)
		count += 1
		
# print the number of value
print 'Counted number: ', count

#print the sum of value inside the file

print 'Sum: ', num

	