import abc
import time


class OddState():
    def display_state(self):
        print("奇数")
    
class EvenState():
    def display_state(self):
        print("偶数")

class CountTime():
    def __init__(self):
        self.count = 0
    def count_up(self):
        self.count += 1
    
    def change_state(self):
        if self.count % 2 == 0:
            return EvenState()
        else:
            return OddState()


if __name__ == '__main__':
    count = CountTime()
    
    while True:
        count.count_up()
        counter = count.change_state()
        print(count.count)
        counter.display_state()
        time.sleep(0.3)
    