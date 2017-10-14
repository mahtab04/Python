##sports = input("Enter your sports name: ").upper()
##team = input("Enter your team name: ").upper()
##if sports == "CRICKET" and team == "INDIA" :
##    print("That's my favourite team")
##elif team == "AUSTRALIA" or team == "ENGLAND" :
##    print("YEAH CRICKET IS BEST")
##else:
##    print("Sorry i dont know the team")
 
#country = input("ENTER YOUR COUNTRY: ").upper()
#pet = input("Enter your pet: ").upper()
#if country== "INDIA" and (pet == "DOG"  or pet == "LION"):
#    print("welcome to india")




ordert= 0
gst = .05
pst = .06
hst = .13


country = input("enter your country: ")
if country .lower() == "india":
    state = input("enter your state: ")
ordert = float(input("enter your order total: "))

if country .lower() == "india":
    if state .lower() == "tamilnadu":
        ordert = ordert + ordert*gst
    elif state.lower() == "delhi" or province.lower() == "kerla" or province.lower() == "bihar" :
        ordert = ordert + ordert*hst
    else:
        ordert = ordert + ordert * pst + ordert * gst
print("Your total including taxes comes to %.2f " % ordert)



























