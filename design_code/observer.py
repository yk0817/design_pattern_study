import abc

class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self,generator):
        pass

class DigitObserver(Observer):
    def update(self,generator):
    
class GraphObserver(Observer):
    def update(self,generator):
    
class NumberGenerator(metaclass=ABCMeta):
    
    def addObserver:
    
    def deleteObserver:
        pass
    
    def notifyObservers:
    
    def getNumber:
    
    def execute