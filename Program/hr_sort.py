'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by
hour of the day for each of the messages. You can pull the hour out from the 'From ' line
by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour 
as shown below.
'''

# Program wrote by Mamadou 21/12/2015

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

new_l = list()
lines = list()
new_h = list()
hour_s = list()
hour = dict()

for line in handle:
    if line.startswith('From '):
        lines = line.rstrip().split(':')
       
        new_l = lines[0]
        
        new_h = new_l.split()
        
        hour_s.append(new_h[5])
        
              
        
    else:
        continue
        
hour_s.sort(reverse=True)

        
'''
for num in hour_s:
            hour_s[num] = hour_s.get(num, 0) + 1                   

'''
for num in hour_s:
    if num not in hour:
        hour[num] = 1
    else:
        hour[num] = hour[num] + 1


for H, N in sorted(hour.items()):
    print  H, N