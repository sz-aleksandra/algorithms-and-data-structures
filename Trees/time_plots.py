from random import randint


def random_list_generator():
    random_digit_list = []
    while len(random_digit_list) <= 10000:
        a = randint(1, 30000)
        if a not in random_digit_list:
            random_digit_list.append(a)
    return random_digit_list

