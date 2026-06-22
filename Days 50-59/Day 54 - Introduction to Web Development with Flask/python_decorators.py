import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # do something before
        function()
        function()
        # do something after

    return wrapper_function


def hello():
    print("Hello")


@delay_decorator
def bye():
    print("Bye")


bye()
