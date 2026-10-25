# Program 9: Algorithm Performance Analysis

import time

def linear_search(arr, key):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            return i, comparisons
    return -1, comparisons


def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == key:
            return mid, comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


arr = list(range(10, 101, 10))
key = int(input("Enter element to search (10-100): "))

print("Array:", arr)

start = time.perf_counter()
pos1, c1 = linear_search(arr, key)
time1 = time.perf_counter() - start

start = time.perf_counter()
pos2, c2 = binary_search(arr, key)
time2 = time.perf_counter() - start

print("\n--- Linear Search ---")
print("Index:", pos1)
print("Comparisons:", c1)
print("Execution Time:", time1, "seconds")
print("Time Complexity: O(n)")

print("\n--- Binary Search ---")
print("Index:", pos2)
print("Comparisons:", c2)
print("Execution Time:", time2, "seconds")
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")