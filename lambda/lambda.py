# Named function
def sum_traditional(x, y):
    return x + y


# Anon function

sum = lambda x, y: x + y

sum(1, 2)


# Garbage collector
# for i in range(1, 1000):
#    a = i
#    print(i)

# 1. Square list ** 2
# Long way
numbers = [1, 2, 3, 4, 5]

squares = []

for n in numbers:
    squares.append(n**2)


# Lambda way
squares = map(lambda x: x**2, numbers)

# 2. Filter list
# Long way
ages = [12, 32, 45, 17, 19]

adults = []

for a in ages:
    if a >= 18:
        adults.append(a)

# Lambda way

adults = filter(lambda x: x >= 18, ages)

# 3. Sort list

people = [
    {"name": "Marco", "age": 21},
    {"name": "Juan", "age": 12},
    {"name": "Luis", "age": 20},
]

sorted_people = sorted(people, key=lambda x: x["age"])

print(sorted_people)

students = [("Marco", 21), ("Juan", 12), ("Luis", 20)]

sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)
