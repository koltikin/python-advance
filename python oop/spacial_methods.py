class Person:
    num_ins = 0

    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        Person.num_ins += 1

    def __call__(self, num1, num2):
        # this method will called the instane is called by it's name
        print("it called __call__ in class Person")
        return num1 + num2

    def __repr__(self):
        # this method will called the instane is print by it's name
        # it is responsable for form of creating instance
        return "Person(first_name,last_name)"
        # return "it called __repr__ in class A"

    def __str__(self):
        # this method will called the instane is print by it's name
        return "it called __srt__ in class Person"

    def __del__(self):
        Person.num_ins -= 1
        # print("item deleted")
        return "it called __del__ in class Person"

    def __add__(obj1, obj2):
        return f"it called __add__ in class Person, and result =  {obj1.first_name} {obj2.first_name}"


a2 = Person("ziya", "kasgari")
a1 = Person("seyfullah", "kasgari")
a3 = Person("jeck", "smth")
del a1
del a2
print(a3(2, 6))
