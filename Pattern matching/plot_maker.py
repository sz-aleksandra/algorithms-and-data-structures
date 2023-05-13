import matplotlib.pyplot as plt
from time import process_time
import gc
from Naive_algorithm import find_N, find_KMP, get_text, get_list_of_words
from kr_algorithm import find_KR


def measure_find_N_times(n_values, list_of_words, text):
    finding_times = []
    gc_old = gc.isenabled()
    gc.disable()
    for n in n_values:
        start_time = process_time()
        for i in range(n):
            find_N(list_of_words[i], text)
        end_time = process_time()
        result = end_time - start_time
        finding_times.append(result)
        print(f"N: {result}")
    if gc_old:
        gc.enable()
    return finding_times


def measure_find_KMP_times(n_values, list_of_words, text):
    finding_times = []
    gc_old = gc.isenabled()
    gc.disable()
    for n in n_values:
        start_time = process_time()
        for i in range(n):
            find_KMP(list_of_words[i], text)
        end_time = process_time()
        result = end_time - start_time
        finding_times.append(result)
        print(f"KMP: {result}")
    if gc_old:
        gc.enable()
    return finding_times


def measure_find_KR_times(n_values, list_of_words, text):
    finding_times = []
    gc_old = gc.isenabled()
    gc.disable()
    for n in n_values:
        start_time = process_time()
        for i in range(n):
            find_KR(list_of_words[i], text)
        end_time = process_time()
        result = end_time - start_time
        finding_times.append(result)
        print(f"KR: {result}")
    if gc_old:
        gc.enable()
    return finding_times


def main():
    n_values = list(range(100, 1100, 100))
    text = get_text('../Sorts/pan-tadeusz-unix.txt')
    list_of_words = get_list_of_words(text)
    plt.figure(figsize=(12, 6))
    plt.plot(n_values, measure_find_N_times(n_values, list_of_words, text), label="Naive algorithm")
    plt.plot(n_values, measure_find_KMP_times(n_values, list_of_words, text), label="KMP algorithm")
    plt.plot(n_values, measure_find_KR_times(n_values, list_of_words, text), label="KR algorithm")
    plt.xlabel("Liczba słów")
    plt.ylabel("Czas wyszukiwania [s]")
    plt.legend()
    plt.savefig('finding_times.png')  # Save the figure to a file
    plt.clf()  # Clear the figure


if __name__ == "__main__":
    main()
