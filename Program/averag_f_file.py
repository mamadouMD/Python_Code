'''
7.2 Write a program that prompts for a file name, then opens that file and reads through 
the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute
 the average of those values and produce an output as shown below.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt 
when you are testing below enter mbox-short.txt as the file name.
'''

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname, 'r')
sumN = 0
count = 0

for line in fh:
    
    if line.startswith("X-DSPAM-Confidence:") :
        count= count + 1    # counting the number of value
        
        num = line[20:27]   # find where numeric value start and record it
        
        num = float(num)    # converting the value into a float
        
        sumN = sumN + num   # adding the value together at any loop

    else:
        continue
        
print "Average spam confidence:", float(sumN)/count