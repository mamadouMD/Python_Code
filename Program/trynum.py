# sample program to demonstrate try/except functionn
# by Mamadou M Diallo

input_N = raw_input('Enter a number:  ')

try:
   input_N2 = int(input_N) # convert the input into integer
except:
   input_N2 = -1

if input_N2 > 0 :
   print 'Nice work'
else:
   print 'Not a number'
