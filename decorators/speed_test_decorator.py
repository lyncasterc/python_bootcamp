from time import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Time elapsed: {end_time-start_time}")
        return result
    return wrapper


@speed_test
def sum_num(a,b):
    return a+b

print(sum_num(2,2))

 


