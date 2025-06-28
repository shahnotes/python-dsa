counter = 0
memo = [None] * 100


def fibonacci(n):
    global counter
    counter += 1
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n):
    global counter
    counter += 1

    if memo[n] is not None:
        return memo[n]

    if n < 2:
        return n

    memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

    return memo[n]
