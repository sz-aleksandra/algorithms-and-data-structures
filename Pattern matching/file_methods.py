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
