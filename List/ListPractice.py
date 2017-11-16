# ask user to enter some name name
# add those names in list
# sort those names in alphabetical order


guest = []

while True:
    Name = input('Enter name: ')
    if Name == "":
        break
    else:
        guest.append(Name)
        print(guest)
guest.sort()
print('the sorted list is')
print(guest)
