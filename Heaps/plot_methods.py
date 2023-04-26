import random
import matplotlib.pyplot as plt
from time import process_time
from Nnary_heap import Nnary_Heap


def generate_number_list(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]


def measure_heap_operations_time(heap, input_list, n_values):
    creation_times = []
    removal_times = []

    for n in n_values:
        # Measure heap creation time
        start_time = process_time()
        for i in range(n):
            heap.push(input_list[i])
        end_time = process_time()
        creation_times.append(end_time - start_time)

        # Measure removal time
        start_time = process_time()
        for _ in range(n):
            heap.pop_root()
        end_time = process_time()
        removal_times.append(end_time - start_time)

    return creation_times, removal_times


def plot_results(n_values, creation_times, removal_times, heap_names):

    for i, heap_name in enumerate(heap_names):
        plt.plot(n_values, creation_times[i], label=heap_name)
    plt.xlabel("Liczba elementów")
    plt.ylabel("Czas tworzenia kopca [s]")
    plt.legend()
    plt.savefig('creation_times.png')  # Save the figure to a file
    plt.clf()  # Clear the figure for the next plot

    # Plot removal times
    plt.figure(figsize=(12, 6))
    for i, heap_name in enumerate(heap_names):
        plt.plot(n_values, removal_times[i], label=heap_name)
    plt.xlabel("Liczba elementów")
    plt.ylabel("Czas usuwania szczytu kopca [s]")
    plt.legend()
    plt.savefig('removal_times.png')  # Save the figure to a file
    plt.clf()  # Clear the figure


def main():
    input_list = generate_number_list(100000, 1, 300000)
    n_values = list(range(10000, 110000, 10000))

    binary_heap = Nnary_Heap(2)
    ternary_heap = Nnary_Heap(3)
    quaternary_heap = Nnary_Heap(4)

    heaps = [binary_heap, ternary_heap, quaternary_heap]
    heap_names = ["Binary Heap", "Ternary Heap", "Quaternary Heap"]

    creation_times = []
    removal_times = []

    for heap in heaps:
        creation_time, removal_time = measure_heap_operations_time(heap, input_list, n_values)
        creation_times.append(creation_time)
        removal_times.append(removal_time)

    plot_results(n_values, creation_times, removal_times, heap_names)


if __name__ == "__main__":
    main()
