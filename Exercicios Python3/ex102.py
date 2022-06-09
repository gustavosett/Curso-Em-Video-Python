def factorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x', end='')
        f *= c
    return f


print(factorial(10, True))