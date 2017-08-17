import abc
import random

class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self,generator):
        pass

class DigitObserver(Observer):
    def update(self,generator):
    
class GraphObserver(Observer):
    def update(self,generator):
    
class NumberGenerator(metaclass=ABCMeta):
    # observer保持
    def __init__(self):
        self.__observers = []
    
    def addObserver(observer):
        self.__observers.append(observer)
    
    def deleteObserver:
        self.__observers.remove(observer)
    
    def notifyObservers:
        for Observer in self.__observers:
            observer.update(self)
    
    @abc.abstractmethod
    def getNumber:
        pass
    
    @abc.abstractmethod
    def execute:
        pass
    
class RandomNumberGenerator(NumberGenerator):
    def __init__(self):
        NumberGenerator.__init__(self)
        self.__number = None
    
    def get_number(self):
        return self.__number
    
    def execute(self):
        for i in range(20):
            self.__number = random.randint(1,50)
            self.notify_observers()

class DigitObserver(Observer):

class GraphObserver(Observer):
