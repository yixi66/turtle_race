import turtle
import time
import random

turtle.bgcolor("rosy brown")



# cathy
cathy = turtle.Turtle()
cathy.shape('turtle')
cathy.color("pink")

# kathy
kathy = turtle.Turtle()
kathy.shape('turtle')
kathy.color('green')

# finish line
cathy.penup()
cathy.pensize(5)
cathy.goto(300,300)
cathy.pendown()
cathy.goto(300,-300)
cathy.write('finish',font=('Arial', 30, "normal"))

# start line
kathy.penup()
kathy.pensize(5)
kathy.goto(-300,300)
kathy.pendown()
kathy.goto(-300,-300)
kathy.write('start',font=('Arial', 30, "normal"))


# cathy back to the start line
cathy.penup()
cathy.goto(-320,200)


# kathy back to the start line
kathy.penup()
kathy.goto(-320,-200)


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

turtle.color("linen")
turtle.penup()
turtle.goto(-200,0)

winner = cathy
if cathy_distance >= 600 and kathy_distance < 600:
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





# cathy.forward(random.choice(distance))
# kathy.forward(random.choice(distance))
# cathy.forward(random.choice(distance))
# kathy.forward(random.choice(distance))
# cathy.forward(random.choice(distance))
# kathy.forward(random.choice(distance))
# cathy.forward(random.choice(distance))
# kathy.forward(random.choice(distance))
# cathy.forward(random.choice(distance))
# kathy.forward(random.choice(distance))
# cathy.forward(random.choice(distance))
# kathy.forward(random.choice(distance))
# cathy.forward(random.choice(distance))
# kathy.forward(random.choice(distance))
# cathy.forward(random.choice(distance))
# kathy.forward(random.choice(distance))


# total_distance = 300

# if cathy.xcor() > 300:
#     cathy.write("cathy win!")
# else:
#     cathy.penup()
#     cathy.goto(-50, 500)
#     cathy.pendown()
#     cathy.write("Distance: ","cathy win!" font=('Arial', 48, "italic"))
#     cathy.end_fill()





# from random import randint
# for i in range(120):
#     cathy.forward(randint(1,10))
#     kathy.forward(randint(1,10))

# if cathy.xcor() > 600:
#     cathy.hideturtle()



turtle.mainloop()
