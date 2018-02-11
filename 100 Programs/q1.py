# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 100 and 500 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

l = []
for i in range(0,501):
    if i%7==0 and i%5!=0:
        l.append(str(i))
print(",".join(l))


