# Python Object-Oriented Programming
# class variable

class Employee:
    """A sample Employee class"""
    num_of_emps = 0
    raise_amount = 1.04   #class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):   #method
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  #can also use Employee.raise_amount

print(Employee.num_of_emps)

emp_1 = Employee('John', 'Smith', 50000)    #instance variable
print(emp_1.num_of_emps)
emp_2 = Employee('Steve', 'Bill', 60000)    #instance variable

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print()
# print(emp_1.__dict__)
# print(Employee.__dict__)
# print()
# print(Employee.raise_amount)    #attribute
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# Employee.raise_amount = 1.05
# print(Employee.raise_amount)    #attribute
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_1.raise_amount = 1.05
# print(Employee.raise_amount)    #attribute
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
print(Employee.num_of_emps)
