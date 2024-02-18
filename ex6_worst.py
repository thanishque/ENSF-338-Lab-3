import random
import timeit
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

linear_avgtimes = []
binary_avgtimes = []

list_lengths = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

for list_length in list_lengths:
    rez_linear = []
    rez_binary = []

    for _ in range(100): 
        numbers = list(range(list_length, 0, -1))  # Generating a sorted array in descending order
        target = 5

        tm_linear = timeit.timeit(lambda: linear_search(numbers, target), number=100)

        random.shuffle(numbers)  
        sorted_numbers = numbers.copy()  
        quicksort(sorted_numbers, 0, len(sorted_numbers) - 1)  
        tm_binary = timeit.timeit(lambda: binary_search(sorted_numbers, target), number=100)

        rez_linear.append(tm_linear)
        rez_binary.append(tm_binary)

    avg_linear = sum(rez_linear) / len(rez_linear)
    avg_binary = sum(rez_binary) / len(rez_binary)

    linear_avgtimes.append(avg_linear)
    binary_avgtimes.append(avg_binary)

# Plotting
plt.plot(list_lengths, linear_avgtimes, marker='o', label='Linear Search')
plt.plot(list_lengths, binary_avgtimes, marker='o', label='Binary Search with Quicksort')

plt.title('Performance of Linear Search vs Binary Search with Quicksort (Worst-case)')
plt.xlabel('Input Size')
plt.ylabel('Average Time (seconds)')
plt.xscale('log')  
plt.yscale('log') 
plt.xticks(list_lengths, list_lengths)  
plt.grid(True)
plt.legend()
plt.show()

# In this code quicksort has the worst complexity 
# as the array is sorted in descending order which would lead to imbalanced partitions
# Binary search with quicksort is a little slower compared to before but it's still faster than linear search
# Same concept applies as the explanation provided in ex6_avg.
