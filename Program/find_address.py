'''
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts
 with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line 
(i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
'''

# Program wrote by Mamadou Fri 12/18/2015

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    
    if line.startswith('From '):
        L= line.rstrip()     # cutting the \n caractere at the right
        new_line = L.split() # splicing the line into word between the space 
        
        print new_line[1] # print the second value inside the list new_list 
        
        count = count + 1 # count the number of line
        
    else:
    	continue

print "There were", count, "lines in the file with From as the first word"
