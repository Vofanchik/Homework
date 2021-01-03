import datetime as dt
from typing import Callable

def fabric_logger_func(log_path):
    def logger_func(func: Callable):
        def log_file(*args, **kwargs):
            with open(log_path, 'w') as f:
                f.write(str(dt.datetime.today()))
                f.write('\n')
                f.write(f'функция {func.__name__}')
                f.write('\n')
                f.write(f'аргументы {args} {kwargs}')
            result = func(*args, **kwargs)
            return result
        return log_file
    return logger_func

@fabric_logger_func(log_path = 'log.txt')
def rec(a, c = 0):
  b = {}
  if c < len(a):
    b[a[c]] =  rec(a, c = c + 1)
  return b
rec(a = ['2018-01-01', 'yandex', 'cpc', 100])





