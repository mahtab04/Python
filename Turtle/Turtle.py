import turtle

# my_turtle = turtle.Turtle()
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.right(100)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.right(100)
# my_turtle.forward(100)
# my_turtle.left(100)
# my_turtle.forward(100)
# my_turtle.right(100)
#  my_turtle.forward(500)






steps = 0
for steps in range(8):
    turtle.forward(100)
    turtle.right(360/8)
print(steps)
for steps in ['red', 'black', 'green', 'cyan' ]:
    turtle.color(steps)
    turtle.forward(100)
    turtle.left(90)


#
# #Declare your variables
# nbrSides = 0
# lengthOfLine = 20
#
# #Ask user how many sides they want for their object
# #Don't forget to convert that value into a integer
# #if you convert to float the for loop will give you an error because range values must be integers
# nbrSides = int(input("How many sides do you want on your object? " ))
#
# #Create a loop to draw the object
# for side in range(0,nbrSides) :
#     turtle.forward(lengthOfLine)
#     #the angle to turn depends on the number of sides of the object
#     turtle.right(360/nbrSides)
#
#     #This is the double bonus challenge, a nested loop that draws a smaller version of the object inside
#     for side in range(0,nbrSides) :
#         turtle.forward(lengthOfLine/2)
#         turtle.right(360/nbrSides)




