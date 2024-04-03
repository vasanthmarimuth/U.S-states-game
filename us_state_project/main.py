import turtle
from turtle import Screen
import pandas

screen = Screen()
screen.title("u.s states game")
image = "blank_states_img.gif"
screen.bgpic(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_text = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state",
                                   prompt="what's another state name?").title()
    if answer_text == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if answer_text in all_states:
        guessed_states.append(answer_text)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_text]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_text)

screen.exitonclick()
