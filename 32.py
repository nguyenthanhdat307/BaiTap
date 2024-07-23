def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))
print(f"LCM of {num1} and {num2} is: {lcm(num1, num2)}")