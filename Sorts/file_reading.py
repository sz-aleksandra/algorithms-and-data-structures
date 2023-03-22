
def read_from_file(filepath):
    with open(filepath, 'r', encoding='utf8') as file_handle:
        lines = [line.rstrip() for line in file_handle]
    return [line for line in lines if line]


def wordlist_from_file(filepath):
    line_list = read_from_file(filepath)
    wordlist = []
    for line in line_list:
        line_wordlist = line.split()
        wordlist += line_wordlist
    return wordlist
