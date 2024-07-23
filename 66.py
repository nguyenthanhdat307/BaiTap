def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = calculate_bmi(weight, height)
print("Your body mass index is: ", bmi)