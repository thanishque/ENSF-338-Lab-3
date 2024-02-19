import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def binary_search(arr, key, low, high):

    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid
    return low

def binary_insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i)
        arr = arr[:j] + [key] + arr[j:i] + arr[i+1:]

def generate_average_case_input(length):

    return [random.randint(1, 1000) for _ in range(length)]

def run_experiment(input_lengths):

    insertion_sort_runtimes = []
    binary_insertion_sort_runtimes = []
    for length in input_lengths:
        arr = generate_average_case_input(length)

        start_time = time.time()
        insertion_sort(arr.copy())
        end_time = time.time()
        insertion_sort_runtimes.append(end_time - start_time)

        start_time = time.time()
        binary_insertion_sort(arr.copy())
        end_time = time.time()
        binary_insertion_sort_runtimes.append(end_time - start_time)
    
    return insertion_sort_runtimes, binary_insertion_sort_runtimes

def plot_results(input_lengths, insertion_sort_runtimes, binary_insertion_sort_runtimes):

    plt.plot(input_lengths, insertion_sort_runtimes, label='Insertion Sort')
    plt.plot(input_lengths, binary_insertion_sort_runtimes, label='Binary Insertion Sort')
    plt.xlabel('Input Length')
    plt.ylabel('Runtime (seconds)')
    plt.title('Comparison of Insertion Sort and Binary Insertion Sort')
    plt.legend()
    plt.show()

input_lengths = [100, 200, 300, 400, 500]
insertion_sort_runtimes, binary_insertion_sort_runtimes = run_experiment(input_lengths)

plot_results(input_lengths, insertion_sort_runtimes, binary_insertion_sort_runtimes)

# binary insertion sort is faster because it takes a binary approach to comparison
# which makes the complexity of comparisons log(n-i) so that leads to a faster search time
# Hence, making binary insertion sort faster when compared to traditional insertion sort. 
