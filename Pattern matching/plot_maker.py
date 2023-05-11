from Naive_algorithm import get_text, get_list_of_words, find_N, find_KMP, find_KR
from time import process_time
import matplotlib.pyplot as plt
import gc


def get_n_first_words(n, words):
    no_duplicates = list(set(words))
    return no_duplicates[:n]


def measure_find_N_timew(n_values, text):
    finding_times = []
    gc_old = gc.isenabled()
    gc.disable()
    for n in n_values:
        first_n_words = get_n_first_words(n, get_list_of_words(text))
        start_time = process_time()
        for word in first_n_words:
            find_N(word, text)
        end_time = process_time()
        finding_times.append(end_time - start_time)
        print(end_time - start_time)
    if gc_old:
        gc.enable()
    return finding_times


def measure_find_KMP_timew(n_values, text):
    finding_times = []
    gc_old = gc.isenabled()
    gc.disable()
    for n in n_values:
        first_n_words = get_n_first_words(n, get_list_of_words(text))
        start_time = process_time()
        for word in first_n_words:
            find_KMP(word, text)
        end_time = process_time()
        finding_times.append(end_time - start_time)
        print(end_time - start_time)
    if gc_old:
        gc.enable()
    return finding_times


def measure_find_KR_timew(n_values, text):
    finding_times = []
    gc_old = gc.isenabled()
    gc.disable()
    for n in n_values:
        first_n_words = get_n_first_words(n, get_list_of_words(text))
        start_time = process_time()
        for word in first_n_words:
            find_KR(word, text)
        end_time = process_time()
        finding_times.append(end_time - start_time)
    if gc_old:
        gc.enable()
    return finding_times


def plot_results():
    n_values = list(range(100, 1100, 100))
    text = get_text('../Sorts/pan-tadeusz-unix.txt')
    plt.figure(figsize=(12, 6))
    plt.plot(n_values, measure_find_N_timew(n_values, text), label="Naive algorithm")
    plt.plot(n_values, measure_find_KMP_timew(n_values, text), label="KMP algorithm")
    plt.plot(n_values, measure_find_KR_timew(n_values, text), label="KR algorithm")
    plt.xlabel("Liczba słów")
    plt.ylabel("Czas wyszukiwania [s]")
    plt.legend()
    plt.savefig('finding_times.png')  # Save the figure to a file
    plt.clf()  # Clear the figure

if __name__ == '__main__':
    plot_results()
