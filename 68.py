num = int(input("Input a four-digit number: "))

x = num // 1000
x1 = (num // 100) % 10
x2 = (num // 10) % 10
x3 = num % 10
sum_digits =  x + x1 + x2 + x3
print(sum_digits)