from file_reading import wordlist_from_file
from SelectionSort.selection_sort import selection_sort
from QuickSort.quick_sort import quick_sort
from BubbleSort.bubble_sort import bubble_sort
from MergeSort.merge_sort import merge_sort
from sys import setrecursionlimit
from time import process_time
import gc
from matplotlib import pyplot as plt


def get_time(path, number_of_words):
    if number_of_words == 0:
        words = wordlist_from_file(path)[:number_of_words]
    else:
        setrecursionlimit(number_of_words)
        words = wordlist_from_file(path)[:number_of_words - 1]
    gc_old = gc.isenabled()
    gc.disable()
    start = process_time()
    selection_sort(words)
    stop = process_time()
    time0 = stop - start
    start = process_time()
    quick_sort(words, 0, len(words) - 1)
    stop = process_time()
    time1 = stop - start
    start = process_time()
    bubble_sort(words)
    stop = process_time()
    time2 = stop - start
    start = process_time()
    merge_sort(words)
    stop = process_time()
    time3 = stop - start
    if gc_old:
        gc.enable()
    return [time0, time1, time2, time3]


def plot_results(path, limit, title):
    keys = []
    x = 0
    y = limit // 5
    while x <= limit:
        keys.append(x)
        x += y
    values0 = [get_time(path, key)[0] for key in keys]
    values1 = [get_time(path, key)[1] for key in keys]
    values2 = [get_time(path, key)[2] for key in keys]
    values3 = [get_time(path, key)[3] for key in keys]
    plt.plot(keys, values0, '-', label='selection sort', markersize=3)
    plt.plot(keys, values1, '-', label='quick sort', markersize=3)
    plt.plot(keys, values2, '-', label='bubble sort', markersize=3)
    plt.plot(keys, values3, '-', label='merge sort', markersize=3)
    plt.legend()
    plt.title(label='')
    figure = plt.gcf()
    figure.savefig(title, format='png')


plot_results('pan-tadeusz-unix.txt', 10000, 'pantadeusz.png')
