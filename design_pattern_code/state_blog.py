import abc
import time


class MetaState(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display_state(self):
        pass

    @abc.abstractmethod
    def display_hira(self):
        pass


class OddState(MetaState):
    def display_state(self):
        print("奇数")

    def display_hira(self):
        print("「きすう」")



class EvenState(MetaState):
    def display_state(self):
        print("偶数")

    def display_hira(self):
        print("「ぐうすう」")


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
        # カウントアップ
        count.count_up()
        # 偶数、奇数で状態変更
        counter = count.change_state()
        print(count.count)
        # 状態に応じた処理
        counter.display_state()
        counter.display_hira()
        time.sleep(0.3)
