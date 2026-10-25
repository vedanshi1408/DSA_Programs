# Program 4: Rabin-Karp Algorithm

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    prime = 101
    base = 256
    pattern_hash = 0
    text_hash = 0
    power = 1
    found = False

    if m > n:
        print("Pattern not found")
        return

    for i in range(m - 1):
        power = (power * base) % prime

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                print("Pattern found at index", i)
                found = True

        if i < n - m:
            text_hash = (
                base * (text_hash - ord(text[i]) * power)
                + ord(text[i + m])
            ) % prime

            if text_hash < 0:
                text_hash += prime

    if not found:
        print("Pattern not found")


text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

rabin_karp(text, pattern)