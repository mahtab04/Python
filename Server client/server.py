import socket

host = '127.0.0.1'
port = 9000
s = socket.socket()
s.bind((host,port))
s.listen(1)
c, addr=s.accept()
print("A client comnected")
while True:
    data =c.recv(1024)
    if not data:
        break
    print("from client: "+str(data.decode()))
    
    data1 = input("enter response: ")

    c.send(data1.encode())
c.close()
