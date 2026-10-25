# Program 2: Hashing Using Linear Probing

size = 5
table = [-1] * size

def insert(key):
    index = key % size

    while table[index] != -1:
        index = (index + 1) % size

    table[index] = key

insert(10)
insert(15)
insert(20)
insert(7)

print("Hash Table:", table)