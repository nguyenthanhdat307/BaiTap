def sum_and_check(a, b):
    sum_result = a + b
    if sum_result in range(15, 20):
        return 20
    else:
        return sum_result

print(sum_and_check(1,2))
print(sum_and_check(10,6))
print(sum_and_check(10,20))