#FavoriteTeam = input("Enter your favorite cricket team? ")
#if FavoriteTeam == "India":
#    print("Yeah,India is the best team.")
#print("India will won the match")
#bonus = None
#deposit = int(input("How much do you to deposit: "))
#if deposit > 100 :
#    bonus = True
#if bonus:
#     print("ENJOY YOUR BONUS")
#print("have a nice day")


user = float(input("Enter your total purchase amount: "))
if user > 50:
    print("The total purchase amout is:", user)
    print("Enjoy your free shipping.")
else:
    shipping = user + 10
    print("The total purchase amount is ", shipping)
