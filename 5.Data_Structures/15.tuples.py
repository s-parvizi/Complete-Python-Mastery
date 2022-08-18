point = (1, 2, 3)
# point = 1, 2, 3
print(point[0:2])
x, y, z = point
print(y)
if 3 in point:
    print("Exists")

another_point = (1, 2) * 3
print("Another Point: ")
print(another_point)

print(tuple("Hello World"))
