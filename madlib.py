# Variables
width = 52
margin = '**'
messages = ['Welcome! Let\'s play MadLibs!', 'Enter a noun, verb, or adjective when propmted.', 'Enter "quit" to exit.']

# Welcome user
print('*' * width)
for message in messages:
    space = width - len(message) - (2 * len(margin))

    if space % 2 == 0:
        print(margin + ' ' * (space//2) + message + ' ' * (space//2) + margin)
    else:
        print(margin + ' ' * (space//2) + message + ' ' * (space//2 + 1) + margin)
print('*' * width)