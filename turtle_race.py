import turtle
import time
import random

  
# ask user 
number_of_times = turtle.textinput("Question", "How many races would you like to see?") 
if number_of_times:
    print("The user want to see", number_of_times, "races")

else:
    print("User don't want to answer.")


turtle.bgcolor("rosy brown")



# cathy
cathy = turtle.Turtle()
cathy.shape('turtle')
cathy.color("pink")

# kathy
kathy = turtle.Turtle()
kathy.shape('turtle')
kathy.color('green')



# start line
kathy.penup()
kathy.pensize(5)
kathy.goto(-300,250)
kathy.pendown()
kathy.goto(-300,-300)

turtle.penup()
turtle.color("gold")
turtle.goto(-310,-330)
turtle.write('start',font=('Arial', 30, "normal"))

# finish line
cathy.penup()
cathy.pensize(5)
cathy.goto(300,250)
cathy.pendown()
cathy.goto(300,-300)

turtle.penup()
turtle.color("gold")
turtle.goto(280,-330)
turtle.write('finish',font=('Arial', 30, "normal"))



# cathy back to the start line
cathy.penup()
cathy.goto(-320,150)


# kathy back to the start line
kathy.penup()
kathy.goto(-320,-150)

# write cathy distance
turtle.color("linen")
turtle.penup()
turtle.goto(-290,300)
turtle.write('Cathy distance: 0', font=('Arial', 20, "normal"))


# write kathy distance
turtle.penup()
turtle.goto(-290,280)
turtle.write('Kathy distance: 0', font=('Arial', 20, "normal"))
turtle.pendown


# ready
time.sleep(1)

# distance
total_distance = 600
cathy_distance = 0
kathy_distance = 0


speeds = [50, 70, 80, 90, 100, 120]
from random import choice
while(cathy_distance < 600 and kathy_distance < 600):
    cathy_speed = random.choice(speeds)
    kathy_speed = random.choice(speeds)

    cathy_distance += cathy_speed
    kathy_distance += kathy_speed

    cathy.forward(cathy_speed)
    kathy.forward(kathy_speed)

    print("cathy_distance: ", cathy_distance)
    print('kathy_distance: ', kathy_distance)



turtle.goto(-200,0)
winner = cathy
if cathy_distance >= 600 and kathy_distance < cathy_distance:
    print(" Cathy  is the winner")
    print("kathy_distance: ",kathy_distance)
    print("cathy_distance: ",cathy_distance)
    turtle.write('Cathy is winner', font=('Arial', 70, "normal"))
    

else:
    print(" Kathy  is the winner")
    print("kathy_distance: ",kathy_distance)
    print("cathy_distance: ",cathy_distance)
    turtle.write('Kathy is winner', font=('Arial', 70, "normal"))


# print(input("how many races would you like to see?  :  "))







turtle.mainloop()
