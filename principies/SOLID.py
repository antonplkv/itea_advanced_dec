#Single Responsibility

####WRONG####
class Employee:
    def __init__(self, name):
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self, name):
        return self._name

    def set_name_db(self):
        "SQL QUERY"
        pass

    def get_name_db(self):
        "SQL QUERY"
        pass
#############



####True
class Employee:
    def __init__(self, name):
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self, name):
        return self._name

class EmployeeDB(Employee):

    def set_name(self):
        "SQL QUERY"
        pass

    def get_name(self):
        "SQL QUERY"
        pass
###



#OpenClosedPrincipe

class Discount:

    def __init__(self, discount):
        self._discount = discount

    def get_discount(self):
        return 10



class TopDiscount(Discount):

    def get_discount(self):
        return 80

class EmployeeDiscount(Discount):

    def get_discount(self):
        return 25


####

#Liskova Substitution Principle

class Figure:

    def __init__(self, *dots):
        self._dots = dots

    def get_dots(self):
        return self._dots

    def write_figure(self, how_to_write=None):

        print('PrintingFigure')


class Triangle(Figure):

    def write_figure(self, how_to_write=None):
        if how_to_write == 'properly':
            print('writing properly')
        else:
            super().write_figure()

class Square(Figure):
    pass


Figure().write_figure()
Triangle().write_figure()


#Interface Segregation Principle

from abc import ABC, abstractmethod

class TriangleI(ABC):

    @abstractmethod
    def paint(self):
        pass


class SquareI(ABC):

    @abstractmethod
    def paint(self):
        pass


class Triangle(TriangleI):
    def paint_triangle(self):
        print('painting')

class Square(SquareI):
    def paint_square(self):
        print('painting')


