# Program 10: DSA Toolkit

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [40, 10, 30, 20, 50]

while True:
    print("\n1.Display  2.Search  3.Sort  4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print("Array:", arr)
    elif choice == "2":
        key = int(input("Enter element: "))
        pos = linear_search(arr, key)
        print("Found at index:", pos if pos != -1 else "Not found")
    elif choice == "3":
        arr = bubble_sort(arr)
        print("Sorted Array:", arr)
    elif choice == "4":
        print("Final Array:", arr)
        break
    else:
        print("Invalid choice")