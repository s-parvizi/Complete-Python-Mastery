# point = {"x": 1, "x": 2}
point = dict(x=1, y=2)
print(point)
print(point["x"])

point["x"]=100
point["z"]=200
print(point)

if "a" in point:
    print(point["a"])
print(point.get("a", 0))

del point["x"]
print(point)

for key in point:
    print(key, point[key])

for x in point.items():
    print(x)

