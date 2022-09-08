numbers = [1, 2, 3]
print(*numbers)

values = list(range(5))
values = [*range(5), *"HELLO"]
print(values)

first = [1, 2, 3]
second = [4, 5, 6]
final = [*first, *second]
print(final)

first_dict = {"x": 1}
second_dict = {"x": 10, "y": 2}
combined = {**first_dict, **second_dict, "z": 3}
print(combined)
