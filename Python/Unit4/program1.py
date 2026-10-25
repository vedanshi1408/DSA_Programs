# Program 1: Hashing Using Chaining

size = 5
table = [[] for i in range(size)]

def insert(key):
    index = key % size
    table[index].append(key)

def display():
    for i in range(size):
        print(i, ":", table[i])

insert(10)
insert(15)
insert(20)
insert(7)

display()