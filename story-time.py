# Story time game (similar to MadLibs) to create a one sentence story

# Start game with question to generate input (first noun)
print('Hello! Let\'s build a story. First, choose a person by first name:')

# collect user input of first noun
first_name = input()

# Continue game with question to grab more input of a food
print('Next, choose a food (just the food. don\'t include \'the\' or \'a\'):')

# Collect user input of a food
food = input()

# Continue game with question to grab more input of a color
print('Thank you! Next, choose a color:')

# Collect user input of a color
color = input()

# Show sentence
print(first_name + " ate the " + color + " " + food + ".")



