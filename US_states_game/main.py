import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# this function allows to h=get the coordinate from the mouse point.
# It was used to form the 50_states.csv, and now it is omitted in the program.
# def get_mouseclick_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouseclick_coor)


all_states = pandas.read_csv("50_states.csv")
states_list = all_states["state"].to_list()
#  or another syntax:
#  states_list = all_states.state.to_list()
correct_answers = []
states_to_learn = []

answer_state = screen.textinput(title="Guess a State", prompt="What is another state name?").title()

while len(correct_answers) < 50:
    if answer_state == "Exit":
        states_to_learn = [state for state in states_list if state not in correct_answers]
        with open("states_to_learn.csv", mode="w") as to_learn:
            to_learn.write(f'You have {len(states_to_learn)} states to learn.\nHere they are: {states_to_learn}')
        break
    elif answer_state in states_list and answer_state not in correct_answers:
        print(f"Yes! There is a state {answer_state} in the list!")
        correct_answers.append(answer_state)
        state_x = int(all_states[all_states.state == answer_state].x.iloc[0])
        state_y = int(all_states[all_states.state == answer_state].y.iloc[0])
        state_coor = (state_x, state_y)
        state_sign = turtle.Turtle()
        state_sign.ht()
        state_sign.penup()
        state_sign.setposition(state_coor)
        state_sign.write(answer_state, move=False, align="center", font=("Arial", 8, "normal"))
        # or another option:
        # state_sign.write(all_states[all_states.state == answer_state].state.item())
        print(correct_answers)

        guessed_states_number = len(correct_answers)

    else:
        print("Mistake...")
        print(correct_answers)

    answer_state = (screen.textinput(title=f"Score {len(correct_answers)}/50", prompt="What is another state name?").
                    title())
