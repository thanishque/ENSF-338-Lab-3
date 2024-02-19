import sys

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid

    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[low + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    # Merge the temporary arrays back into arr[low:high+1]
    i = j = 0
    k = low

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Set recursion limit to avoid stack overflow
sys.setrecursionlimit(20000)

# Given input vector
arr = [8, 42, 25, 3, 3, 27, 3]
# Perform merge sort
merge_sort(arr, 0, len(arr) - 1)
# Output sorted array
print("Sorted array:", arr)
