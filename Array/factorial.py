def factorial(N):

    if N == 1 or N == 0:
        return "1"

    fact = 1
    for i in range(2, N + 1):
        fact *= i

    return str(fact)


print(factorial(5))
