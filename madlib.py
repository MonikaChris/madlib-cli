import re

# Variables
width = 52
margin = '**'
messages = ['Welcome! Let\'s play MadLibs!',
            'Enter a noun, verb, or adjective when propmted.',
            'Enter "quit" to exit.']
playing = True

# Welcome user
print('*' * width)
for message in messages:
    space = width - len(message) - (2 * len(margin))

    if space % 2 == 0:
        print(
            margin + ' ' * (space // 2) + message + ' ' * (space // 2) + margin)
    else:
        print(margin + ' ' * (space // 2) + message + ' ' * (
                    space // 2 + 1) + margin)
print('*' * width)


# Functions
def read_template(file):
    try:
        with open(file, 'r') as reader:
            return reader.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)


def parse_template(text):
    pattern = r"[{][^}]+[}]"

    stripped = re.sub(pattern, '{}', text)

    parts_list = re.findall(pattern, text)
    parts = []

    for part in parts_list:
        parts.append(part[1:-1])

    return stripped, tuple(parts)


def merge(text, subs):
    return text.format(*subs)


def save_madlib(text):
    with open('assets/my_madlib.txt', 'w') as writer:
        writer.writelines(text)


while playing:

    text = read_template('assets/make_me_a_video_game.txt')

    template = parse_template(text)

    libs = []
    for word in template[1]:
        user_word = input(f'{word}? ')
        if user_word == 'quit':
            playing = False
            break
        else:
            libs.append(user_word)

    madlib = merge(template[0], libs)
    print(madlib)
    save_madlib(madlib)

    playing = False




