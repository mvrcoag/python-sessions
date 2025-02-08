# Primitives
string = "Hola"
integers = 5
floats = 5.54321
boolean = True

# Lists
string_lists = ["Hola", "Juan", "Y", "Pedro"]
integer_lists = [1, 2, 3, 4]
mixed_lists = ["Hola", 5, "Mudo", True, 5.5]

mixed_lists[0]

# Dict
integers_dict = {"Marco Antonio": 21, "Pedro": 12}
strings_dict = {"A": "B", "C": "D"}

# Complex objects
people_list = [{"name": "Marco", "age": 21}, {"name": "Luis", "age": 20}]

# Way 1: one line

# Way 2: two lines
person = people_list[0]

people_dict = {"names": ["Marco", "Luis"], "ages": [21, 20]}

# Vectors
v1 = [1, 2, 3]
v2 = [4, 5, 6]
v3 = [7, 8, 9]
v4 = [10, 11, 12]

# Matrix
A = [v1, v2]
B = [v3, v4]

# Matrix addition
# C = A + B
# C_ij = A_ij + B_ij


def sum_m(A, B):
    if len(A) != len(B):
        return None

    C = []

    for i in range(len(A)):
        C.append([])

        for j in range(len(A[i])):
            sum = A[i][j] + B[i][j]
            C[i].append(sum)

    return C


print(sum_m(A, B))

# Matrix substraction
# C = A + B
# C_ij = A_ij - B_ij


def sub_m(A, B):
    if len(A) != len(B):
        return None

    C = []

    for i in range(len(A)):
        C.append([])

        for j in range(len(A[i])):
            sub = A[i][j] - B[i][j]
            C[i].append(sub)

    return C


print(sub_m(A, B))

# Matrix Multiplication aka dot
# C_ij = sum(A_ik, B_kj)
# If A cols == B Rows

A = [[1, 2, 3], [4, 5, 6]]

B = [[7, 8], [9, 10], [11, 12]]

# C matrix 2 * 2


def dot_m(A, B):
    if len(A[0]) != len(B):
        return None

    C = []

    for _ in range(len(A)):
        C.append([0] * len(B[0]))

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C


print(dot_m(A, B))

import numpy as np

print(np.dot(A, B))
