def dec(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        return value + 10
    return wrapper


@dec
def print_some(x, y):
    return x + y


print(print_some(10, 10))
