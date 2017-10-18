#Create a program that asks the user for a number and then prints out a list of all the divisors of that number

num = int(input("Enter a number: "))
b = []
if num == 0:
    print("Enter a number more than 0")
for i in range(1, num+1, 1):
    if num % i == 0:
        b.append(i)
print(b)