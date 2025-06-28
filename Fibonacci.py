counter = 0

def fibonacci(n):
    global counter
    counter += 1
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
