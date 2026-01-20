marks = [22, 30, 40, 50]
print(marks)
new_marks = []

for x in marks:
    new_marks.append(x + 2)
print(new_marks)


# list comprehensions

marks = [22, 30, 40, 50]
new_marks = [x + 2 for x in marks]
print(new_marks)


# qs 2
cubes = []
for x in range(10):
    if x % 2 == 0:
        cubes.append(x **3)
print(cubes)

## list comp..
cubes = [x ** 3 for x in range(10) if x % 2 == 0]
print(cubes)