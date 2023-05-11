def get_text(path):
    text = ''
    with open(path, 'r', encoding='utf8') as file_handle:
        for line in file_handle:
            text += line
    return text


def get_list_of_words(text):
    alphabet = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźżAĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSTUVWXYZŹŻ'
    words = []
    word = ''
    for character in text:
        if character in alphabet:
            word += character
        elif word:
            words.append(word)
            word = ''
    words = list(set(words))
    return words


#print(get_text('../Sorts/pan-tadeusz-unix.txt'))


def find_N(string, text):
    position_list = []
    pos_in_text = 0
    while pos_in_text <= len(text) - len(string):
        pos_in_string = 0
        while pos_in_string < len(string) and text[pos_in_text + pos_in_string] == string[pos_in_string]:
            pos_in_string += 1
        if pos_in_string == len(string):
            position_list.append(pos_in_text)
            pos_in_text += len(string)
        else:
            pos_in_text += 1
    return position_list


def create_KMP_table(string):
    KMP_table = [0, 0]
    k = 0
    for pos_in_kmp in range(1, len(string)):
        while k > 0 and string[k] != string[pos_in_kmp]:
            k = KMP_table[k]
        if string[k] == string[pos_in_kmp]:
            k += 1
        KMP_table.append(k)
    return KMP_table


def find_KMP(string, text):
    KMP_table = create_KMP_table(string)
    position_list = []
    pos_in_text = 0
    while pos_in_text <= len(text) - len(string):
        pos_in_string = KMP_table[0]
        while pos_in_string < len(string) and text[pos_in_text + pos_in_string] == string[pos_in_string]:
            pos_in_string += 1
        if pos_in_string == len(string):
            position_list.append(pos_in_text)
        pos_in_text += max(1, pos_in_string - KMP_table[pos_in_string])
    return position_list


def find_KR(string, text):
    pass

#example_text = 'lokomotywmotywa'
#xample_string = 'motyw'
#print(find_N(example_string, example_text))
#print(find_KMP(example_string, example_text))

