# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

n = int(input("Enter number: "))
if n % 2 == 1 or n in range(6, 21):
    print("Weird")
else:
    print("Not Weird")
