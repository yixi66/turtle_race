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
cathy.goto(-300,200)
cathy.pendown()

# kathy back to the start line
kathy.penup()
kathy.goto(-300,-200)

time.sleep(2)


distance = [50, 70, 80, 90, 100, 120]
from random import choice
while cathy.xcor() <= 300 and kathy.xcor <= 300:
    cathy.forward(random.choice(distance))
    kathy.forward(random.choice(distance))


if cathy.xcor() > kathy.xcor():
    print("cathy win!")
else:
    print("kathy win!")


cathy.clear()
kathy.clear()

print(input"how many races would you like to see?  :  ")


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
