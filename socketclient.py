#This code is a python client using the socket library. This will connect to a remote or local host and send "Say something" Back to the user. Try setting up a server with a netcat client to test.

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 4242)
s.send(b'Say something: ') # b tag added in python3 to indicate bytes not strings
data = s.recv(1024)          
s.close()
print('Received', data)
