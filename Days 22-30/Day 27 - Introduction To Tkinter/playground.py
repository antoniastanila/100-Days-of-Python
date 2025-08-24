def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(n=2, add=3, multiply=5)
