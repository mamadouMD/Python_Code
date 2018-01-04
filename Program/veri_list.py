'''
8.4 Open the file romeo1.txt and read it line by line. For each line, split the line into a
list of words using the split() function. The program should build a list of words.For each
word on each line check to see if the word is already in the list and if not append it to
the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
'''

# Program wrote by Mamadou Fri 12/18/2015

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()   # create a empty list variable

for line in fh:
    line = line.rstrip().split() # taking the line and eliminating the last news line caracter and splicing the line into words
    
    for word in line:
        
        if word not in lst: # verify if the word is not already inside list to add it
            lst.append(word)
        else:
            continue
            
lst.sort()    # sorting the words into alphabetical order

print lst