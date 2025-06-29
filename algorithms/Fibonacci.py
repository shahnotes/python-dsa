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


def fibonacci_bottom_up(n):
    fib_list = [0, 1]
    global counter
    for i in range(2, n + 1):
        counter += 1
        next_fib = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_fib)
    return fib_list[n]
