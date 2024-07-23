def sum_of_first_n_integers(n):
      return n * (n + 1) // 2

n = int(input("Input a number: "))
result = sum_of_first_n_integers(n)
print(result)