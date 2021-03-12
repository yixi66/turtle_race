import turtle
import time
import random
from turtle import Screen
turtle.title('Turtle Race')
  
height = 360
width = 360
screen = Screen()
screen.screensize(width, height)


# ask user 
number_of_times = turtle.textinput("Question", "How many races would you like to see?") 

if number_of_times:
    print("The user wants to see", number_of_times, "races")
else:
    number_of_times = 1
    print("User doesn't want to answer.")



race_time = 1
# write the result
cathy_win = 0
kathy_win = 0

while race_time <= int(number_of_times):
    turtle.clearscreen()

    height = 360
    width = 360
    screen = Screen()
    screen.screensize(width, height)


    # background color
    turtle.bgcolor("rosy brown")


    # cathy setting
    cathy = turtle.Turtle()
    cathy.shape('turtle')
    cathy.color("pink")

    # kathy setting
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

# ready
    time.sleep(1)


    # distance
    total_distance = 620
    cathy_distance = 0
    kathy_distance = 0

    # turtles move
    speeds = [50, 70, 80, 90, 100, 120]
    from random import choice
    while(cathy_distance < 620 and kathy_distance < 600):
        cathy_speed = random.choice(speeds)
        kathy_speed = random.choice(speeds)

        cathy_distance += cathy_speed
        kathy_distance += kathy_speed

        cathy.forward(cathy_speed)
        kathy.forward(kathy_speed)





    turtle.goto(-200,0)
    winner = cathy
    if cathy_distance >= 600 and kathy_distance < cathy_distance:
        print(" Cathy  is the winner")
        print("kathy_distance: ",kathy_distance)
        print("cathy_distance: ",cathy_distance)
        turtle.write('Cathy is winner', font=('Arial', 70, "normal"))
        cathy_win = cathy_win + 1

    else:
        print(" Kathy  is the winner")
        print("kathy_distance: ",kathy_distance)
        print("cathy_distance: ",cathy_distance)
        turtle.write('Kathy is winner', font=('Arial', 70, "normal"))
        kathy_win = kathy_win + 1

    print("cathy_win: ",cathy_win)
    print("kathy_win: ",kathy_win)

        # write cathy distance
    turtle.color("linen")
    turtle.penup()
    turtle.goto(-290,300)
    turtle.write('Cathy distance: ' + str(cathy_distance), font=('Arial', 20, "normal"))

        # write kathy distance
    turtle.penup()
    turtle.goto(-290,280)
    turtle.write('Kathy distance: ' + str(kathy_distance), font=('Arial', 20, "normal"))
    turtle.pendown

# see the result
    time.sleep(1)

    cathy_win_percentage = (cathy_win / race_time) * 100
    kathy_win_percentage = (kathy_win / race_time) * 100
    print("cathy win precentage: ", cathy_win_percentage, "%")
    print("kathy win precentage: ", kathy_win_percentage, "%")
 

    race_time = race_time + 1






#close 
turtle.exitonclick()


turtle.mainloop()
