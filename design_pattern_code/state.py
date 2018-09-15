
"""参考URL"""
# https://github.com/faif/python-patterns/blob/master/behavioral/state.py

class State():
    
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("scan station is {} {}".format(self.stations[self.pos],self.name))

class AmState(State):
    
    def __init__(self,radio):
        self.radio = radio
        self.stations = ["1250","1380","1510"]
        self.pos = 0
        self.name = "AM"
    
    def toggle_amfm(self):
        print("switching to fm")
        self.radio.state = self.radio.fmstate

class FmState(State):
    
    def __init__(self,radio):
        self.radio = radio
        self.stations = ["81.3","89.1","103.9"]
        self.pos = 0
        self.name = "FM"
    
    def toggle_amfm(self):
        print("switching to am")
        self.radio.state = self.radio.amstate

class Radio(object):
    
    def __init__(self):
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate
    
    def toggle_amfm(self):
        self.state.toggle_amfm()
    
    def scan(self):
        self.state.scan()

if __name__ == '__main__':
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    actions *= 2
    
    for action in actions:
        # Stateのクラスに状態変数を持たせている事がわかる。
        # 状態に応じた処理を分割して記述していることで
        # 条件分岐に応じた処理 → 条件分岐・処理 の2つに分けて考えられる。
        # ↑条件分岐や処理項目が多い時に有効
        print(radio.state.pos)
        action()
        