# Program 8: Array Operations

arr = [10, 20, 30, 40, 50]

while True:
    print("\n1.Display  2.Insert  3.Delete")
    print("4.Search   5.Update  6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print("Array:", arr)

    elif choice == "2":
        value = int(input("Enter value: "))
        pos = int(input("Enter position: "))
        if 1 <= pos <= len(arr) + 1:
            arr.insert(pos - 1, value)
            print("Element inserted:", arr)
        else:
            print("Invalid position")

    elif choice == "3":
        pos = int(input("Enter position: "))
        if 1 <= pos <= len(arr):
            print("Deleted:", arr.pop(pos - 1))
            print("Array:", arr)
        else:
            print("Invalid position")

    elif choice == "4":
        value = int(input("Enter element to search: "))
        if value in arr:
            print("Found at position:", arr.index(value) + 1)
        else:
            print("Element not found")

    elif choice == "5":
        pos = int(input("Enter position: "))
        if 1 <= pos <= len(arr):
            arr[pos - 1] = int(input("Enter new value: "))
            print("Updated array:", arr)
        else:
            print("Invalid position")

    elif choice == "6":
        print("Final Array:", arr)
        break

    else:
        print("Invalid choice")