# *****************decorate class with class ****************
class decrator:
    def __init__(self, other_class):
        self.other_class = other_class

    def __call__(self, fname, lname, age):
        class inner(self.other_class):
            def __init__(self, fname, lname, age):
                super().__init__(fname, lname)
                self.age = age

        return inner(fname, lname, age)


@decrator
class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def say_hello(self):
        print(f"hello {self.first_name}")


# p0 = Person("jac", "sophy")
# print(p0.first_name)
# p1 = Person("jac", "sophy", 25)
# print(p1.age, p1.first_name)
# p1.say_hello()

# *****************decorate function with class ****************
class decrator1:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, num1, num2, num3):
        def inner(num1, num2, num3):
            result = self.fun(num1, num2) * num3
            print(result)

        return inner(num1, num2, num3)


@decrator1
def my_fun(num1, num2):
    # print(num1 + num2)
    return num1 + num2


# my_fun(5, 10)
# my_fun(5, 10, 7)

# *****************decorate class with function ****************
def decorator3(class_name):
    class inner(class_name):
        def __init__(self, fname, lname, age):
            super().__init__(fname, lname)
            self.age = age

    return inner


@decorator3
class Studen:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def say_hello(self):
        print(f"hello {self.first_name}")


# s1 = Studen("Tom", "Black")

# print(s1.first_name, s1.last_name, sep="\n")

s2 = Studen("Tom", "Black", 33)

print(s2.first_name, s2.last_name, s2.age, sep="\n")

s2.say_hello()
