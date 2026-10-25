# Program 10: Strassen's Matrix Multiplication

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

a, b = A[0]
c, d = A[1]

e, f = B[0]
g, h = B[1]

# Seven products
p1 = a * (f - h)
p2 = (a + b) * h
p3 = (c + d) * e
p4 = d * (g - e)
p5 = (a + d) * (e + h)
p6 = (b - d) * (g + h)
p7 = (a - c) * (e + f)

# Calculate result matrix
C = [
    [p5 + p4 - p2 + p6, p1 + p2],
    [p3 + p4, p1 + p5 - p3 - p7]
]

print("Resultant Matrix:")
for row in C:
    print(row)