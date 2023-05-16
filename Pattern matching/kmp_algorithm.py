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
    position_list = []
    if not (string and text):
        return position_list
    if len(string) > len(text):
        return position_list
    if len(string) == len(text) and string != text:
        return position_list

    KMP_table = create_KMP_table(string)

    pos_in_text = 0
    while pos_in_text <= len(text) - len(string):
        pos_in_string = KMP_table[0]
        while pos_in_string < len(string) and text[pos_in_text + pos_in_string] == string[pos_in_string]:
            pos_in_string += 1
        if pos_in_string == len(string):
            position_list.append(pos_in_text)
        pos_in_text += max(1, pos_in_string - KMP_table[pos_in_string])
    return position_list
