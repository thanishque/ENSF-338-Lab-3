import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Bubble sort with counts
def bubble_sort_with_counts(arr):
    comparisons = swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return comparisons, swaps

# Generate average-case input
def generate_input(size):
    return random.sample(range(size), size)

# Run the code on inputs of increasing size
sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800]
comparisons_results = []
swaps_results = []


for size in sizes:
    comparisons_list = []
    swaps_list = []
    for _ in range(10):
        arr = generate_input(size)
        comparisons, swaps = bubble_sort_with_counts(arr)
        comparisons_list.append(comparisons)
        swaps_list.append(swaps)
    comparisons_results.append(np.mean(comparisons_list))
    swaps_results.append(np.mean(swaps_list))

# Plotting results
plt.figure(figsize=(12, 6))

# Plot comparisons
plt.subplot(1, 2, 1)
plt.plot(sizes, comparisons_results, marker='o', label='Comparisons', color='blue')
plt.xlabel('Input Size')
plt.ylabel('Comparisons')
plt.title('Comparisons in Bubble Sort')

# Interpolating function for comparisons
f_comp = interp1d(sizes, comparisons_results, kind='cubic')
x_new = np.linspace(min(sizes), max(sizes), 100)
plt.plot(x_new, f_comp(x_new), '--', color='blue', label='Interpolating Function')

plt.legend()
plt.grid(True)

# Plot swaps
plt.subplot(1, 2, 2)
plt.plot(sizes, swaps_results, marker='o', label='Swaps', color='orange')
plt.xlabel('Input Size')
plt.ylabel('Swaps')
plt.title('Swaps in Bubble Sort')

# Interpolating function for swaps
f_swaps = interp1d(sizes, swaps_results, kind='cubic')
plt.plot(x_new, f_swaps(x_new), '--', color='orange', label='Interpolating Function')

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

#Used ChatGPT for this exercise