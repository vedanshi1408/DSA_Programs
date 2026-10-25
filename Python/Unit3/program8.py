# Program 8: Min Heap

import heapq

heap = []

while True:
    print("\n1. Insert  2. Delete Min  3. Display  4. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        value = int(input("Enter value: "))
        heapq.heappush(heap, value)

    elif ch == "2":
        if heap:
            print("Deleted:", heapq.heappop(heap))
        else:
            print("Heap is empty")

    elif ch == "3":
        print("Min Heap:", heap)

    elif ch == "4":
        break

    else:
        print("Invalid choice")