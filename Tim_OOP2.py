# class Person:
#     number_of_people = 0   #class attribute
#
#     def __init__(self, name):
#         self.name = name
#         Person.add_person()
#
#     @classmethod
#     def number_of_people_(cls):
#         return cls.number_of_people
#
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1
#
# p1 = Person("Tim")
# p2 = Person("Jill")
# print(Person.number_of_people_())


# print(p1.number_of_people)
# print(Person.number_of_people)
# Person.number_of_people = 8
# print(p2.number_of_people)
#
# p1.number_of_people = 10
# print(Person.number_of_people)
# print(p1.number_of_people)


class Math:

    @staticmethod
    def add5(x):
        return x+5

    @staticmethod
    def pr():
        print('run')

print(Math.add5(7))
Math.pr()
