# Python Object-Oriented Programming

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def test_method(self):
        pass

    def fullname(self):   #method
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith', 50000)    #instance variable
emp_2 = Employee('Steve', 'Bill', 60000)    #instance variable


print(emp_1.first)
print(emp_1.email)
print()
print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname())     #fullname is a method, #if @property is added, then no ()
print(emp_2.fullname())     #for instance emp_2, no need to put self in ()
print()
print(Employee.fullname(emp_1))           #for class Employee, you need to give instance
