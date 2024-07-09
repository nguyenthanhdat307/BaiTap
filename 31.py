import math

def compute_gcd(a, b):
    return math.gcd(a, b)

num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))

gcd_result = compute_gcd(num1, num2)
print(f"gcd(num1, num2):{gcd_result}")