import socket


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ask for  a connection request 
mysock.connect(('www.py4inf.com', 80))

# Send a connection request
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
	data =  mysock.recv(512)
	if (len(data) < 1):
		break
	print data;
#Close the connection
mysock.close()



