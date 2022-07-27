import abc
from abc import ABCMeta  # , abstractstaticmethod agora está deprecado


# "I" antes do nome da classe indica que é uma interface


class IPerson(metaclass=abc.ABCMeta):

    # "@abstractstaticmethod@ e "@abc.abstractstaticmethod" Está deprecado desde 3.3
    @staticmethod
    @abc.abstractmethod
    def person_method():
        """ Interface Method"""


class Student(IPerson):

    def __init__(self):
        self.name = "Generic Student Name"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):

    def __init__(self):
        self.name = 'Genericc Teacher Name'

    def person_method(self):
        print("I am a teacher")


# p1 = IPerson()
# p1.person_method()

# s1 = Student()
# s1.person_method()
# t1 = Teacher()
# t1.person_method()

class PersonFactory:

    @staticmethod
    def buildperson(person_type):
        if person_type == 'Student':
            return Student()
        if person_type == 'Teacher':
            return Teacher()
        print('Invalid Type')
        return -1


if __name__ == '__main__':
    # choice = input("What type of person do you want to create?\n")
    # person = PersonFactory.buildperson(choice)
    person = PersonFactory.buildperson(input("What type of person do you want to create?\n"))
    person.person_method()
