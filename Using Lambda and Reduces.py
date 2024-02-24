from functools import reduce

factorial_reduce = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))

# Example usage:
number = 5
fact = factorial_reduce(number)
print("Factorial of", number, "is", fact)
