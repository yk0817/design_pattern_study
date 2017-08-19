import abc
import time
    
        
class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display_state(self):
        pass

class OddState(State):
    def display_state(self):
        print("奇数")
    
class EvenState(State):
    def display_state(self):
        print("偶数")

class CountTime(object):
    # self.count = 0
    def __init__(self):
        self.count = 0
    def count_up(self):
        self.count += 1

if __name__ == '__main__':
    count = CountTime()
    
    while True:
        count.count_up()
        if count.count % 2 == 0:
            EvenState().display_state()
        else:
            OddState().display_state()
        time.sleep(1)
