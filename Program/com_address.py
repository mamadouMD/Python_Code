''''
	9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the
greatest number of mail messages. The program looks for 'From ' lines and takes the second
word of those lines as the person who sent the mail. The program creates a Python 
dictionary that maps the sender's mail address to a count of the number of times they 
appear in the file. After the dictionary is produced, the program reads through the 
dictionary using a maximum loop to find the most prolific committer.
'''

# Program wrote by Mamadou Fri 12/19/2015

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short1.txt"
handle = open(name, 'r')

lst = list()
name = list()
data = dict()

'''
assigning the word inside the data( key) to 0 and its value to 0
'''
com_word = None
big_count = None


for line in handle:
    if line.startswith('From '):
        new_l = line.rstrip()
        lst = new_l.split()
       
        name.append(lst[1])
        
#print name

''' 
A loop to look if the word is not inside the data to add it and assign a value of 1 
else to increment the value by 1 

	it is possible to chance these next 5 line by 
	for word in name:
		name[word] = name.get(word, 0) + 1
'''

for word in name:  
    if word not in data:
        data[word] = 1
    else:
        data[word] = data[word] + 1
        
#print data

'''
loop to assign the word to address and count to number of apperence
'''

for word, count in data.items(): 
    #print word, count
    
    if big_count is None or count > big_count:
        
        big_word = word
        big_count = count
        
print big_word, big_count