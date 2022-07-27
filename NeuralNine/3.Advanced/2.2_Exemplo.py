import time

def timed(function):

    def wrapper(*args, **kwargs):
        b4 = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {format(after-b4, '.2f')} seconds to execute")
        return value

    return wrapper

@timed
def myfunc(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

myfunc(50000)
