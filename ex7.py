import json
import time
import numpy as np
import matplotlib.pyplot as plt

# Load data and tasks
with open('ex7data.json', 'r') as f:
    data = json.load(f)
with open('ex7tasks.json', 'r') as f:
    tasks = json.load(f)

# Binary search function
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Timing function
def time_binary_search(arr, target, first_midpoint):
    times = []
    for mid in range(first_midpoint, len(arr), len(arr) // 10):
        start_time = time.time()
        result = binary_search(arr, target, mid, len(arr) - 1)
        end_time = time.time()
        times.append((mid, end_time - start_time))
    return times

# Perform search tasks and choose best midpoints
best_midpoints = {}
for target in tasks:
    target_name = str(target)
    for value in data:
        if target == value:
            first_midpoint = len(data) // 2  # Default midpoint
            search_times = time_binary_search(data, target, first_midpoint)
            best_midpoint, _ = min(search_times, key=lambda x: x[1])
            best_midpoints[target_name] = best_midpoint
            break  # Move to the next target

# Visualize results
plt.figure(figsize=(10, 6))
for target in tasks:
    target_name = str(target)
    if target_name in best_midpoints:  # Check if a best midpoint was chosen for this target
        midpoints = []
        times = []
        times.extend(time_binary_search(data, target, best_midpoints[target_name]))
        midpoints.extend([best_midpoints[target_name]] * len(times))  # Ensure same length for midpoints and times
        print("Midpoints:", midpoints)
        print("Times:", [t[1] for t in times])
        plt.scatter(midpoints, [t[1] for t in times], label=target_name)

plt.title('Binary Search Performance with Configurable Midpoints')
plt.xlabel('Midpoint')
plt.ylabel('Time (s)')
plt.grid(True)
plt.show()
