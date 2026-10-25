# Program 6: Huffman Coding

import heapq
from itertools import count

def huffman_coding(chars, freq):
    serial = count()
    heap = []

    for char, frequency in zip(chars, freq):
        heapq.heappush(heap, (frequency, next(serial), char))

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)

        heapq.heappush(
            heap, (f1 + f2, next(serial), (left, right))
        )

    codes = {}

    def generate(node, code=""):
        if isinstance(node, str):
            codes[node] = code or "0"
            return

        generate(node[0], code + "0")
        generate(node[1], code + "1")

    generate(heap[0][2])

    print("Character : Huffman Code")
    for char in chars:
        print(char, ":", codes[char])

chars = ['A', 'B', 'C', 'D']
freq = [5, 9, 12, 13]

huffman_coding(chars, freq)