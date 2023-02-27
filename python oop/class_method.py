"make class method from a function outside class"


def fun(obj):  # first argument must be the class it self
    print(obj.name, "what is your name?")


class A:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    name = "hello"


# the fun automaticly takes the class A as the first argument then return the class method
# A.greating = classmethod(fun)
# a1 = A("ziya", "kasgari")
# a1.greating()


# make class method inside class
class B:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    @classmethod
    def make_instance(cls, str):
        fname, lname = str.split("-")
        return cls(fname, lname)


b1 = B.make_instance("ziya-kasgari")
b2 = B("abdulhabir", "akyol")
b3 = b2.make_instance("yusuf-eymen")
# print(b3.last_name)
