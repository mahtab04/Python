filename = "demo1.txt"
WRITE = 'w'
myfile = open(filename, WRITE)
for index in range(10):
    name = input('enter the name')
    age = input('Enter age')
    myfile.write(name + "," + age + "\n")
myfile.close()
