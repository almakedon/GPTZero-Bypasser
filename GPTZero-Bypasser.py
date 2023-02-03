import random

def replace_letters(file_buffer):
    # Changes all AEOaeo letters with the cyrillic varients.
    file_buffer = file_buffer.replace('a', '𝚊')
    file_buffer = file_buffer.replace('q', '𝚚')
    file_buffer = file_buffer.replace('u', '𝚞')
    file_buffer = file_buffer.replace('n', '𝚗')
    file_buffer = file_buffer.replace('t', '𝚝')
    file_buffer = file_buffer.replace('m', '𝚖')
    file_buffer = file_buffer.replace('c', '𝚌')
    file_buffer = file_buffer.replace('o', '𝚘')
    file_buffer = file_buffer.replace('l', '𝚕 ')
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
