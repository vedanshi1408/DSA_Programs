# Program 1: Linear Search with Performance Analysis

def linear_search(arr, key):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1

        print("Checking element:", arr[i])

        if arr[i] == key:
            return i, comparisons

    return -1, comparisons


def display_array(arr):
    print("Array elements:", arr)


# Main Program
arr = [10, 20, 30, 40, 50, 60, 70]

print("LINEAR SEARCH")
display_array(arr)

key = int(input("Enter element to search: "))

position, comparisons = linear_search(arr, key)

if position != -1:
    print("Element found at index:", position)
    print("Position in array:", position + 1)
else:
    print("Element not found")

print("Total comparisons:", comparisons)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")