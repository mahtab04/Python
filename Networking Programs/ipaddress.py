# knowing ip address of a website
import socket

# take the server name
host = 'http://www.todaytvseries.com/'
try:
    addr = socket.gethostbyname (host)  # know the ip address of website
    print ('IP Address= ' + addr)
except socket.gaierror:  # if get address info error occurs
    print ("The website doesn't exists")


