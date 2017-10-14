
import datetime
userinput = 0
nbrdays = 0
currentDate = datetime.date.today()
userinput = input("Enter your project date (mm/dd/yyyy):")
projectdate = datetime.datetime.strptime(userinput, "%m/%d/%Y").date()
#print(projectdate)
deadline = projectdate - currentDate
nbrweeks = deadline.days / 7
nbrdays = deadline.days % 7

print("You have %d weeks " % nbrweeks + "and %d days" % nbrdays)
