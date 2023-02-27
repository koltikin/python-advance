" python property decrator, python setter, getter, delter methodes"

"if we want to decide some properties value after object creation"


class A:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def getemail(self):
        return self._email  # must named property start with '_'

    def setemail(self, new_email):
        self._email = new_email

    def delemail(self):
        del self._email

    email = property(getemail, setemail, delemail, "this is the email property")


# a1 = A("ziya", "kasgari")
# a1.email = "koltikin210@gmail.com"
# print(a1.first_name)
# print(a1.email)

class B:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @email.deleter
    def email(self):
        del self._email


b1 = B("ziya", "kasgari")
b1.email = "ziya@gmail.com"
print(b1.email)
print(b1.first_name)
print(b1.last_name)

"if we need some properties from existing properties"


class C:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        fname, lname = value.split(" ")
        self.first_name = fname
        self.last_name = lname


# c1 = C("ziya", "kasgari")
# c1.full_name = "abdullah ali"
# print(c1.full_name)
# print(c1.first_name)
# print(c1.last_name)
