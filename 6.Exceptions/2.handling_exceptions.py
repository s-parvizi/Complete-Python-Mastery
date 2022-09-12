try:
    file = open("2.handling_exceptions.py")
    age = int(input("Age:"))
    x_factor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown.")
finally:
    file.close()
print("Execution continues.")
