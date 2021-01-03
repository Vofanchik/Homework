import datetime as dt
from typing import Callable
import requests


def fabric_logger_func(log_path):
    def logger_func(func: Callable):
        def log_file(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(log_path, 'w') as f:
                f.write(str(dt.datetime.today()))
                f.write('\n')
                f.write(f'функция {func.__name__}')
                f.write('\n')
                f.write(f'аргументы {args} {kwargs}')
                f.write('\n')
                f.write(f'возвращает {result}')
            result = func(*args, **kwargs)
            return result
        return log_file
    return logger_func

@fabric_logger_func(log_path = 'log.txt')
def list_to_dict(*args):
    li = args
    if len(li) > 0:
      di = {li[-1]}
      for item in li[-2:-len(li)-1 :-1]:
        di = {item : di}
    return di

list_to_dict('2018-01-01', 'yandex', 'cpc', 100)





