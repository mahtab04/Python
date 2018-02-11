# SAMPLE INPUT 
# 2 #no of test case
# 5 14
# 3 21
# SAMPLE OUTPUT 
# No
# Yes








t = int(input())#no of test case
for i in range(t):
    a,b = map (int, input().split())
    if b%a==0:
        print("Yes")
    else:
        print("No")