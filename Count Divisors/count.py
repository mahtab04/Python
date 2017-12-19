# You have been given 3 integers - l, r and k. Find how many numbers between l and r (both inclusive) are divisible by k.
# You do not need to print these numbers, you just have to find their count.
# SAMPLE INPUT
# 1 10 1
# SAMPLE OUTPUT
# 10
print ('Hello World')
l = int (input ())
r = int (input ())
k = int (input ())
count = 0
for i in range (l, r + 1):
    if i % k == 0:
        count += 1
print (count)
