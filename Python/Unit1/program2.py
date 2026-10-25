# Program 2: Binary Search with Performance Analysis

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        print("Checking middle element:", arr[mid])

        if arr[mid] == key:
            return mid, comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


# Main Program
arr = [10, 20, 30, 40, 50, 60, 70]

print("BINARY SEARCH")
print("Sorted Array:", arr)

key = int(input("Enter element to search: "))

position, comparisons = binary_search(arr, key)

if position != -1:
    print("Element found at index:", position)
    print("Position in array:", position + 1)
else:
    print("Element not found")

print("Total comparisons:", comparisons)
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")