from functools import wraps


def val_checker(condit_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            _val_result = condit_func(*args)
            if not _val_result:
                raise ValueError(f'wrong val: {args}')
            else:
                 return func(*args)
        return wrapper
    return _val_checker


def check_func(x):
    return x > 0


@val_checker(check_func)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube.__name__)
print(calc_cube.__doc__)
