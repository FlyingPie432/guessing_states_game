import turtle
import pandas as pd
screen = turtle.Screen()
screen.title('U.S states Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_states = screen.textinput(f'{len(guessed_states)} / 50 States Correct', "what's another state's name").title()
    if answer_states == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_states in all_states:
        guessed_states.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_states]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_states, align='center', font=('Arial', 12, 'normal'))
