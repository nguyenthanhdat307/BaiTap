def sum_three_numbers(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c
print(sum_three_numbers(2, 1, 2))
print(sum_three_numbers(3, 2, 2))
print(sum_three_numbers(2, 2, 2))
print(sum_three_numbers(1, 2, 3))