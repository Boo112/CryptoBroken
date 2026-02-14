
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result


def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

# TODO: refactor this

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper


def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

