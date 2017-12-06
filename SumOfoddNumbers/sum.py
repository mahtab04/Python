# An efficient solution is to use direct formula. To find the sum of first
# n odd numbers we can apply odd number theorem,
# it states that the sum of first n odd numbers is equal to the square of n.
#
# let n = 10, therefore sum of first 10 odd numbers is
#
# 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = 100
#
# if we apply odd number theorem:
#
# sum of first 10 odd numbers = n * n = 10 * 10 = 100.



def Oddsum(n):
    return n*n


n = 5
print("Sum ",Oddsum(n))