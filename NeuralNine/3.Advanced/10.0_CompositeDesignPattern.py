import abc
from abc import ABCMeta


class IDepartment(metaclass=ABCMeta):

    @abc.abstractmethod
    def __init__(self, employees):
        """ Implement in child class """

    @staticmethod
    @abc.abstractmethod
    def print_department():
        """ Implement in child class"""


class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f'Account Department: {self.employees} employees')


class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f'Dev Department: {self.employees} employees')


class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print(f"Parent Dptm. Base Employees : {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f'Total No. of employees: {self.employees}.')


dept1 = Accounting(200)
dept2 = Development(160)

parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()