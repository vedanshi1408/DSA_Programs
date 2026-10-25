# Program 5: Insertion Sort with Performance Analysis

def insertion_sort(arr):
    comparisons = 0
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        print("\nPass", i)
        print("Element to insert:", key)

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

        print("Array after pass:", arr)

    print("\nTotal comparisons:", comparisons)
    print("Total shifts:", shifts)


# Main Program
arr = [64, 25, 12, 22, 11]

print("INSERTION SORT")
print("Original Array:", arr)

insertion_sort(arr)

print("\nSorted Array:", arr)
print("Best Case Time Complexity: O(n)")
print("Average Case Time Complexity: O(n^2)")
print("Worst Case Time Complexity: O(n^2)")
print("Space Complexity: O(1)")