import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet:", "Which turtle will win the race? Enter a colour: ")
colours = ["red", "green", "blue", "orange", "purple", "yellow"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colours[i])
    new_turtle.goto(-230, y_pos[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f" You've won! The {winning_turtle} tutle is the winner!")
            else:
                print(f" You've lost! The {winning_turtle} tutle is the winner!")
                is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
