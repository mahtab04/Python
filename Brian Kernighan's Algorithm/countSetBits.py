def countsetbits(n):
    count =0

    while n:
        n=n &(n-1)
        count = count+1
    return count



t =int(input())#no of test case
for i in range(t):
    num = int(input())#enter the number to find set bits
    print(countsetbits(num))

