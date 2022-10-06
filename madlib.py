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


def read_template(file):
    with open(file, 'r') as reader:
        return reader.read()


def parse_template(text):
    pattern = r"[{]\w+[}]"

    stripped = re.sub(pattern, '{}', text)

    parts_list = re.findall(pattern, text)
    parts = []

    for part in parts_list:
        parts.append(part[1:-1])

    return stripped, tuple(parts)

def merge(text, subs):
    return text.format(*subs)


# while playing:



