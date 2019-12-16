from abc import ABC, abstractmethod

class Vehicle(ABC):

    attr = 1

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def beep(self):
        print('Default beep')

class Car(Vehicle):

    def move(self):
        print('Moving')

    def beep(self):
        print('Car beep')


print(dir(Vehicle))


Car().move()
Car().beep()


class MyABC:

    def my_method(self):
        raise NotImplementedError


class MyClass(MyABC):
    pass


