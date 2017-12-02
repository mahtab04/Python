# Python program to illustrate union
# Maintained repetition

print ("Union of a list")


def Union(lst1, lst2):
    final_list = lst1 + lst2
    return final_list


# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20, 52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print (Union (lst1, lst2))
print ("\n")

print ('Union list in sorted order')


# Python program to illustrate union
# Maintained repetition and order
def Union(lst1, lst2):
    final_list = sorted (lst1 + lst2)
    return final_list


# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20, 52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print (Union (lst1, lst2))
print ("\n")

print ('Union Of List without repetition')


# Python program to illustrate union
# Without repetition
def Union(lst1, lst2):
    final_list = list (set (lst1) | set (lst2))
    return final_list


# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20, 52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print (Union (lst1, lst2))
print ('\n')

print ("Union of three list")


# Python program to illustrate union
# Union of three lists
def Union(lst1, lst2, lst3):
    final_list = list (set ().union (lst1, lst2, lst3))
    return final_list


# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20, 52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
lst3 = [4, 78, 5, 6, 9, 25, 64, 32, 59]
print (Union (lst1, lst2, lst3))
