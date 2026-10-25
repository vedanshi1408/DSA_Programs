# Program 6: Linear Search vs Binary Search Comparison

def linear_search(arr, key):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            return i, comparisons

    return -1, comparisons


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
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


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("SEARCHING ALGORITHM COMPARISON")
print("Sorted Array:", arr)

key = int(input("Enter element to search: "))

linear_position, linear_count = linear_search(arr, key)
binary_position, binary_count = binary_search(arr, key)

print("\n--- Linear Search ---")
if linear_position != -1:
    print("Element found at index:", linear_position)
else:
    print("Element not found")
print("Comparisons:", linear_count)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

print("\n--- Binary Search ---")
if binary_position != -1:
    print("Element found at index:", binary_position)
else:
    print("Element not found")
print("Comparisons:", binary_count)
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")

print("\n--- Final Comparison ---")
print("Linear Search Comparisons:", linear_count)
print("Binary Search Comparisons:", binary_count)

if linear_count < binary_count:
    print("Linear Search used fewer comparisons.")
elif binary_count < linear_count:
    print("Binary Search used fewer comparisons.")
else:
    print("Both used the same number of comparisons.")