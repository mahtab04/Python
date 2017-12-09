n = int(input("Enter a number: "))
rev = 0
while(n>0):

    div = n%10
    rev = rev*10+div
    n = n//10

print("The Reverse nummber is: ",rev)