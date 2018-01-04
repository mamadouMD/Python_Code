'''
5.2 Write a program that repeatedly prompts a user for integer numbers until the user 
enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put 
out an appropriate message and ignore the number. Enter the numbers from the book for 
problem 5.1 and Match the desired output as shown.
'''

largest = None
smallest = None
	
while True:
    num = raw_input("Enter a number: ")
    if num == "done":break
    
    try:
        num2 = int(num)
    except:
        print "Invalid input"
        continue
    
    if largest is None or largest < num2:
		largest = num2
    if smallest is None or smallest > num2:
		smallest = num2 

    
print "Maximum is", largest
print "Minimun is", smallest

'''inp = list()
try:
	while True:
		num = raw_input("Enter a number: ")
	 	if num == "done":break
	 	
	 	inp.append(int(num))
    	#inp = map(int, num.splice()) 
    	
    	for num2 in inp:
	    	if largest is None or largest < num2:
	    		largest = num2
	    	if smallest is None or smallest > num2:
	    		smallest = num2 
except:
        print "Invalid input"

print "Maximum is", largest
print "Minimun is", smallest'''