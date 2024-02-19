import time
import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    done = False
    while not done:
        while i <= j and arr[i] <= pivot:
            i += 1
        while arr[j] >= pivot and j >= i:
            j -= 1
        if j < i:
            done = True
        else:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def run_quicksort_worst_case(input_sizes):
    runtimes = []
    for size in input_sizes:

        arr = list(range(size, 0, -1))
        
        start_time = time.time()
        quicksort(arr, 0, size - 1)
        end_time = time.time()
        
        runtime = end_time - start_time
        runtimes.append(runtime)
    return runtimes

input_sizes = [100, 200, 300, 400, 500]

runtimes = run_quicksort_worst_case(input_sizes)

plt.plot(input_sizes, runtimes, label='Quicksort Worst Case')
plt.xlabel('Input Size')
plt.ylabel('Runtime (seconds)')
plt.title('Quicksort Worst Case Complexity')
plt.legend()
plt.show()
