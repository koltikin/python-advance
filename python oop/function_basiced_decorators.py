# function basiced decorator -------------------
# add some functionality to the functions


def decorator(fun):
    def wrapper_fun(*args, **kwargs):
        print(f"before {fun.__name__}")
        fun(*args, **kwargs)
        print(f"after {fun.__name__} is excuted")

    return wrapper_fun


@decorator
def my_sum_fun(num1, num2):
    print(num1 + num2)


# my_sum_fun(5, 6)


# modefy existing functions


def three_times(fun):
    def wrapper_fun(*args, **kwargs):
        result = fun(*args, **kwargs)
        for i in range(3):
            print(result)

    return wrapper_fun


def decorator1(fun):
    def wrapper_fun(num1, num2, num3):
        result = fun(num1, num2) * num3
        return result

    return wrapper_fun


@three_times
@decorator1
def my_sum_fun(num1, num2):
    result = num1 + num2
    return result


my_sum_fun(5, 3, 8)
