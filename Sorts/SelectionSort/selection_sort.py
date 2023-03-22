def change_element_positions(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def selection_sort(words):
    for i in range(len(words)):
        earliest_word_index = i
        for j in range(i, len(words)):
            if words[j] < words[earliest_word_index]:
                earliest_word_index = j
        change_element_positions(words, i, earliest_word_index)
