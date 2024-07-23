def convert_distance(feet):

    inches = feet * 12
    yards = feet / 3.0
    miles = feet / 5280.0
    return inches, yards, miles
feet_distance = float(input("Input distance in feet: "))
inches, yards, miles = convert_distance(feet_distance)

print(f"{inches} inches")
print(f"{yards} yards")
print(f"{miles} miles")