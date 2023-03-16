
def read_from_file(filepath):
    with open(filepath, 'r') as file_handle:
        lines = [line.rstrip() for line in file_handle]
    return [line for line in lines if line]


def line_division_to_wordlist(linelist):
    wordlist = []
    for line in linelist:
        line_wordlist = line.split()
        wordlist += line_wordlist
    return wordlist


print(line_division_to_wordlist(read_from_file('pan-tadeusz-unix.txt')))