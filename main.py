import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
jacky = turtle.Turtle()
jacky.penup()
jacky.hideturtle()

data = pandas.read_csv("50_states.csv")
df = pandas.DataFrame(data)

list_of_answers = []
value = 0
while value < 50:
    answer_state = screen.textinput(title=f"{value}/50 correct", prompt="What's another state's name?")
    for i in df["state"]:
        if answer_state.title() == i:
            x = df._get_value(df[df["state"] == i].index[0], "x")
            y = df._get_value(df[df["state"] == i].index[0], "y")
            jacky.goto(x, y)
            jacky.write(answer_state)
            list_of_answers.append(answer_state)
        lf = pandas.DataFrame(list_of_answers)
        lf.to_csv("answer_count.csv")
        value = len(lf)




screen.exitonclick()
