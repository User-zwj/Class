# object oriented programming in python

# string = 'hello'

# print(string.upper())
# print(string.capitalize())

# class Dog:
#
#     def __init__(self, name):
#         self.name = name     #attribute
#         print(name)
#
#     def add_one(self, x):
#         return x+1
#
#     def bark(self):    #method
#         print('bark')

# d = Dog()    #instance/object
# d.bark()
# print(d.add_one(5))

# d = Dog('Tim')
# print(d.name)
# d2 = Dog('Bill')
# print(d2.name)


# class Dog:
#
#     def __init__(self, name, age):
#         self.name = name     #attribute
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, x):
#         self.age = x

# d = Dog('Tim', 24)
# d2 = Dog('Bill', 11)
# print(d.get_name())
# print(d2.get_name())
# print(d.get_age())
# print(d2.get_age())
# d.set_age(10)
# print(d.get_age())






##=======================
class Pet:  #upper level class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("I am %s and I am %s years old" % (self.name, self.age))

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self, name, age, color):
        # super().__init__(name, age)      #####
        self.name = name
        self.age = age
        self.color = color

    def speak(self):    #overwrite speak in the upper level class
        print('meow')

    def show(self):
        print("I am %s and I am %s years old and I am %s" % (self.name, self.age, self.color))

class Dog(Pet):
    def speak(self):
        print('Bark')

# class Fish(Pet):
#     pass

# p = Pet('Tim', 19)
# p.show()
# p.speak()

c = Cat('Bill', 34, 'white')
c.show()
# c.speak()

# f = Fish('Bubble', 10)
# f.speak()
