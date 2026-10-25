# Program 5: KMP Algorithm

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    found = False

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            print("Pattern found at index", i - j)
            found = True
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    if not found:
        print("Pattern not found")


text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

if pattern:
    kmp_search(text, pattern)
else:
    print("Pattern cannot be empty")