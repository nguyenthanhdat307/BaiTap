def feet_and_inches_to_cm(feet, inches):
    total_inches = feet * 12 + inches
    cm = total_inches * 2.54
    return cm

feet = int(input("input feet: "))
inches = int(input("input inches: "))

centimeters = feet_and_inches_to_cm(feet, inches)
print(f'{centimeters} centimet')