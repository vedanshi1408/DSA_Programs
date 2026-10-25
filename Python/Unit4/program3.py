# Program 3: Naive String Matching

def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    found = False

    for i in range(n - m + 1):
        j = 0

        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            print("Pattern found at index", i)
            found = True

    if not found:
        print("Pattern not found")

text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

naive_search(text, pattern)