import random

def replace_letters(file_buffer):
    # Changes all AEOaeo letters with the cyrillic varients.
    file_buffer = file_buffer.replace(' ', '‎ ')
    return file_buffer

def insert_zwj(file_buffer):
    output = ""
    zwj = "\u200D" # Zero Width Joiner unicode character
    for char in file_buffer:
        output += char
        # Randomly insert zero width joiner
        if random.random() < 0.2: # Lower number = Less ZWJ
            output += zwj
    return output


print(insert_zwj(replace_letters(input())))

input()
