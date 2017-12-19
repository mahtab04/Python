# # Searching an element in a list/array in python
# # can be simply done using 'in' operator
# # Example:
# # if x in arr:
# # print arr.index(x)
#
# # If you want to implement Linear Search in python
#
# # Linearly search x in arr[]
# # If x is present then return its location
# # else return -1
#
# def search(arr, x):
#     for i in range(len(arr)):
#
#         if arr[i] == x:
#             return i
#
#     return -1
#
#
# arr = [46, 76, 8, 5, 3, 2, 23, 90]
# x = 90
# found = search(arr, x)
# print("the element found at",found)
#




test=int(input())
for i in range(test):
    word1 = str(input());

    numVowel = 0
    for vowel in word1:
        if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u":
            numVowel += 1
        if vowel == "A" or vowel == "E" or vowel == "I" or vowel == "O" or vowel == "U":
            numVowel += 1
    print(numVowel)