import abc
import random
import time


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self,generator):
        pass

    
class NumberGenerator(metaclass=abc.ABCMeta):
    # observer保持
    def __init__(self):
        self.__observers = []
    
    def addObserver(self,observer):
        self.__observers.append(observer)
        # print(self.__observers)
    
    def deleteObserver(self,observer):
        self.__observers.remove(observer)
    
    def notifyObservers(self):
        for observer in self.__observers:
            # print(observer)
            print(self)
            # observer.update(self)
    
    @abc.abstractmethod
    def getNumber(self):
        pass
    
    @abc.abstractmethod
    def execute(self):
        pass
    
class RandomNumberGenerator(NumberGenerator):
    def __init__(self):
        NumberGenerator.__init__(self)
        self.__number = None
    
    def getNumber(self):
        return self.__number
    
    def execute(self):
        for i in range(20):
            self.__number = random.randint(0, 49)
            self.notifyObservers()

class DigitObserver(Observer):
    def update(generator):
        print("DigitObserver:{}".format(generator.get_number()))
        time.sleep(1)

class GraphObserver(Observer):
    def update(self,generator):
        count = generator.get_number()
        print("graphobserver:")
        for i in range(count):
            print("*")
        time.sleep(1)

if __name__ == "__main__":
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.addObserver(observer1)
    generator.addObserver(observer2)
    generator.execute()
    
