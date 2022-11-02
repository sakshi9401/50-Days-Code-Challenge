class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("Displaying name and id number")
        print(self.name)
        print(self.idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
class Employee(Person):
        def __init__(self, name, idnumber, salary, post):
            self.salary = salary
            self.post = post
            Person.__init__(self, name, idnumber)
        def details(self):
            print("My name is {}".format(self.name))
            print("IdNumber: {}".format(self.idnumber))
            print("Post: {}".format(self.post))
name = input("Enter your Name ")
idnum = int(input("Enter your ID Number "))
salary = int(input("Enter your monthly salary "))
post = input("State your Post ")
a = Employee(name, idnum, salary, post)
a.display()
a.details()
