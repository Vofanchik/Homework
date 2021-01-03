from typing import Callable

def print_dec(old_func: Callable):
    def new_func(*args, **kwargs):
        print(f'вызвана {old_func.__name__}')
        print(f'c арг {args}, {kwargs}')
        result = old_func(*args, **kwargs)
        print(f'получили {result}')
        return result
    return new_func()

@print_dec
def mult(a, b):
    return a + b

mult(2, 3)