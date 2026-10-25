# Program 7: Sorting Algorithms Comparison

def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return comparisons, swaps


def selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return comparisons, swaps


def insertion_sort(arr):
    comparisons = 0
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return comparisons, shifts


original = [64, 25, 12, 22, 11]

print("SORTING ALGORITHMS COMPARISON")
print("Original Array:", original)

bubble_arr = original.copy()
b_comp, b_swaps = bubble_sort(bubble_arr)
print("\n--- Bubble Sort ---")
print("Sorted Array:", bubble_arr)
print("Comparisons:", b_comp)
print("Swaps:", b_swaps)
print("Time Complexity: O(n^2)")

selection_arr = original.copy()
s_comp, s_swaps = selection_sort(selection_arr)
print("\n--- Selection Sort ---")
print("Sorted Array:", selection_arr)
print("Comparisons:", s_comp)
print("Swaps:", s_swaps)
print("Time Complexity: O(n^2)")

insertion_arr = original.copy()
i_comp, i_shifts = insertion_sort(insertion_arr)
print("\n--- Insertion Sort ---")
print("Sorted Array:", insertion_arr)
print("Comparisons:", i_comp)
print("Shifts:", i_shifts)
print("Time Complexity: O(n^2)")

print("\n--- Final Comparison ---")
print("Bubble Sort comparisons:", b_comp)
print("Selection Sort comparisons:", s_comp)
print("Insertion Sort comparisons:", i_comp)
print("All algorithms produce the same sorted array.")