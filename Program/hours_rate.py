'''
4.6 Write a program to prompt the user for hours and rate per hour 
using raw_input to compute gross pay. Award time-and-a-half for 
the hourly rate for all hours worked above 40 hours. 
Put the logic to do the computation of time-and-a-half in 
a function called computepay() and use the function to do the computation. 
The function should return a value. Use 45 hours and a rate of 10.50 per hour 
to test the program (the pay should be 498.75). You should use raw_input to read a string 
and float() to convert the string to a number. Do not worry about error checking the user 
input unless you want to - you can assume the user types numbers properly.
'''

# program wrote by Mamadou M Diallo
# email mouctar1991@yahoo.fr
# December 14 2015   

def computepay(h,r):
    h = float(h) # convert the value into float
    r = float(r)
    
    if h > 40:
        h1 = 40      # Hours worked during regular hours
        h2 = h - 40  # Hours workd during extra hours
        r2 = r*1.50  # The new rate for the extra hours
        
        pay = h1*r + h2*r2 
        
    else:
        pay = float(h)*float(r)
    
    
    return pay 

hrs = raw_input("Enter Hours:")
rte = raw_input("Enter The Rate Per Hour: ")

p = computepay(hrs, rte)
print 'pay 'p