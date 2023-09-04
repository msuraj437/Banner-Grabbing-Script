import socket 

s = socket.socket()

ip = input('Enter the IP address: ')
port = str(input('Enter the port number: '))

s.connect((ip, int(port)))

print(s.recv(1024))

