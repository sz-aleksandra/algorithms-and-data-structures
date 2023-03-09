import argparse
from ast import arg
import sys

MORSE = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '.--.',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
}


def read_text(path):
    text = []
    with open(path, 'r') as file_handle:
        line = file_handle.readline().rstrip()
        while line != '':
            text.append(line)
            line = file_handle.readline().rstrip()
    return text


def translate_to_morse(path):
    text = read_text(path)
    text_in_morse = []
    for line in text:
        line_in_morse = ''
        words = line.split()
        for word in words:
            word_in_morse = ''
            for char in word:
                char = char.lower()
                if char.isalpha():
                    word_in_morse += f"{MORSE.get(char)} "
            if word_in_morse:
                line_in_morse += word_in_morse
                line_in_morse += '/ '
        text_in_morse.append(line_in_morse[:-3])
    return text_in_morse


def print_text(text):
    print('\n'.join(text))

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    print_text(translate_to_morse(args.file))


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)