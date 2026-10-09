import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. State Game')
image = 'blank_states_img.gif'
screen.addshape(image)
end_game = True
turtle.shape(image)

answer_state = screen.textinput(title='Guess the State', prompt="What's another states's name?")
cap_answer = answer_state.capitalize()


data = pandas.read_csv('50_states.csv')
data_dict = data.to_dict()

states = data['state'].to_list()
print(states)

if cap_answer in states:
    print('Your answer is correct')


turtle.mainloop()