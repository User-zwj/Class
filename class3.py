# Python Object-Oriented Programming
# regular method(self), class method(cls), static method()

class Employee:
    """A sample Employee class"""
    num_of_emps = 0
    raise_amount = 1.04   #class variable

    def __init__(self, first, last, pay):   #self indicates instance
        self.first = first    #instance variable
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):   #method on instance
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  #can also use Employee.raise_amount

    @classmethod    #decorator
    def set_raise_amount(cls, amount):   #work on class instead of instance
        cls.raise_amount = amount

    @classmethod    #use classmethod as alternative constructor
    def from_string(cls, emp_str):       #starting with 'from' is a convention
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)         #cls indicates Employee

    @staticmethod    #if it doesn't include instance, class anywhere
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('John', 'Smith', 50000)    #instance variable
emp_2 = Employee('Steve', 'Bill', 60000)    #instance variable

# Employee.set_raise_amount(1.05)    #class method, set class variable to 1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_1.set_raise_amount(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


###############################
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
#
# # first, last, pay = emp_str_1.split('-')
# # new_emp_1 = Employee(first, last, pay)
# # print(new_emp_1.email)
# # print(new_emp_1.pay)
#
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)


##########
import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))
