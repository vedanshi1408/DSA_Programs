# Program 3: Bubble Sort with Performance Analysis

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        swapped = False

        print("\nPass", i + 1)

        for j in range(n - i - 1):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

            print("Checking:", arr)

        print("Array after pass:", arr)

        if not swapped:
            break

    print("\nTotal comparisons:", comparisons)
    print("Total swaps:", swaps)


# Main Program
arr = [64, 25, 12, 22, 11]

print("BUBBLE SORT")
print("Original Array:", arr)

bubble_sort(arr)

print("\nSorted Array:", arr)
print("Best Case Time Complexity: O(n)")
print("Average Case Time Complexity: O(n^2)")
print("Worst Case Time Complexity: O(n^2)")
print("Space Complexity: O(1)")