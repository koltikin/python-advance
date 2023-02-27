def my_fun():
    print("hello")


arg = [("ziy", 33, "istanbul"), ("ziy", 33, "istanbul")]
# print(type(arg))


def my_fun1(*arg):
    # convert the arg to tuple: ([('ziy', 33, 'istanbul'), ('ziy', 33, 'istanbul')])
    print(type(arg))
    print(len(arg))  # len(arg) shoud be 1
    for var in arg:
        # type var shoud be [('ziy', 33, 'istanbul'), ('ziy', 33, 'istanbul')]  list
        print(type(var))
        for in_var in var:
            # type in_var shoud be ('ziy', 33, 'istanbul'), ('ziy', 33, 'istanbul') tuple
            print(type(in_var))
            print(in_var)


# my_fun1("ziy", 33, "istanbul")

# my_fun1(arg)


arg = [("ziy", 33, "istanbul"), ("ziy", 33, "istanbul")]
# print(*arg, sep="\n")  # * user for unpack now *arg == ('ziy', 33, 'istanbul'), ('ziy', 33, 'istanbul')


def my_sum(*arg):
    result = 0
    for var in arg:
        result += var
    return result


# print(my_sum(5, 6, 8, 7, 9, 8))


list1 = [5, 6, 7, 8]
list2 = [9, 10, 11, 12]
list3 = [13, 14, 15, 16]

# print(my_sum(*list1, *list2, *list3))

a, *b, c = 5, 1, 2, 3, 4, 6
# print(b, type(b), a, c)

a = [*"hello world"]  # unpack "hello world" to h,e,l,l  ,w,o,r,l,d
# print(*a, type(a))


my_dict = {"name": "ziya", "age": 33, "place": "istanbul"}
your_dict = {"name": "abdullah", "age": 30, "place": "istanbul"}

# print({**my_dict, **your_dict})  # adding two dictionary with **


def my_second_fun(**kwargs):
    print(type(kwargs))
    print(kwargs.items())
    print(kwargs["name"])
    print(kwargs["age"])
    print(kwargs["place"])


profile_dict = {"name": "ziya", "age": 36, "place": "istanbul"}
newvar = {"name": "ziya", "age": 36, "place": "istanbul"}

# my_second_fun(name='ziya', age=36, place='istanbul')
# my_second_fun(**profile_dict)
