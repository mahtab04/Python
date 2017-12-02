FileName = 'demo.txt'
WRITE = 'w'
# APPEND = 'a'
file = open(FileName, WRITE)
file.write("HELLO\n")
file.write('hi how r u')
file.close()