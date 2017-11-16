# Given a number N, the task is to print all factorial numbers smaller than or equal to N.
# Example:
# Input:
# 2 # number of inputs
# 2
# 6
#
# Output:
# 1 2
# 1 2 6



t = int(input("Enter no of inputs").strip())
while (t > 0):
    fact = 1
    n = int(input())
    for i in range(1, n + 1):
        fact = fact * i
        if fact > n:
            break
        print(fact, end=' ')
    print()
    t -= 1
