def get_text(path):
    text = ''
    with open(path, 'r', encoding='utf8') as file_handle:
        for line in file_handle:
            text += line
    return text


#print(get_text('../Sorts/pan-tadeusz-unix.txt'))


def find_N(string, text):
    position_list = []
    pos_in_text = 0
    while pos_in_text < len(text) - len(string):
        pos_in_string = 0
        does_it_match_possibly = True
        while does_it_match_possibly and pos_in_string < len(string):
            if text[pos_in_text + pos_in_string] != string[pos_in_string]:
                does_it_match_possibly = False
            else:
                pos_in_string += 1
        if does_it_match_possibly:
            position_list.append(pos_in_text)
            pos_in_text += len(string)
        else:
            pos_in_text += 1
    return position_list


#example_text = 'lokomotywamotywa'
#example_string = 'motyw'

#print(find_N(example_string, example_text))