# Program 4: Selection Sort with Performance Analysis

def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        min_index = i

        print("\nPass", i + 1)
        print("Current Array:", arr)

        for j in range(i + 1, n):
            comparisons += 1

            print("Comparing", arr[j], "with", arr[min_index])

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
            print("Swapped:", arr)

        print("Array after pass:", arr)

    print("\nTotal comparisons:", comparisons)
    print("Total swaps:", swaps)


# Main Program
arr = [64, 25, 12, 22, 11]

print("SELECTION SORT")
print("Original Array:", arr)

selection_sort(arr)

print("\nSorted Array:", arr)
print("Best Case Time Complexity: O(n^2)")
print("Average Case Time Complexity: O(n^2)")
print("Worst Case Time Complexity: O(n^2)")
print("Space Complexity: O(1)")