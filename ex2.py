import timeit
import matplotlib.pyplot as plt
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def generate_input(size, case):
    if case == 'best':
        return list(range(size))
    elif case == 'worst':
        return list(range(size, 0, -1))
    elif case == 'average':
        return random.sample(range(size), size)

sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

# Perform tests and generate performance plots
plt.figure(figsize=(8, 6))
for case in ['best', 'worst', 'average']:
    results = {'bubble': [], 'quick': []}
    for size in sizes:
        arr = generate_input(size, case)
        
        bubble_time = timeit.timeit(lambda: bubble_sort(arr.copy()), number=1)
        results['bubble'].append(bubble_time)
        
        quick_time = timeit.timeit(lambda: quick_sort(arr.copy()), number=1)
        results['quick'].append(quick_time)

    plt.plot(sizes, results['bubble'], label=f'Bubble Sort - {case}')
    plt.plot(sizes, results['quick'], label=f'Quick Sort - {case}')

plt.title('Performance of Bubble Sort vs Quick Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()
# Used ChatGPT for this assignment