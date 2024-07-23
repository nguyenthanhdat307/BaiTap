def check_numbers(a, b):
    return a == b or abs(a - b) == 5 or a + b == 5
print(check_numbers(2, 3))
print(check_numbers(8, 2))   
print(check_numbers(3, 3))   
print(check_numbers(2, -3))  
print(check_numbers(20, 5))