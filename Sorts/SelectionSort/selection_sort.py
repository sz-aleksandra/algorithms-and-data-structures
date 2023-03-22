from change_position import change_element_positions


def selection_sort(words):
    for i in range(len(words)):
        earliest_word_index = i
        for j in range(i, len(words)):
            if words[j] < words[earliest_word_index]:
                earliest_word_index = j
        change_element_positions(words, i, earliest_word_index)
