import time
# 参考
# https://github.com/faif/python-patterns/blob/master/structural/proxy.py

class SalesManager:
    def talk(self):
        print("sales manager ready to talk")

class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def talk(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
            self.safes = SalesManager()
            time.sleep(0.1)
            self.safes.talk()
        else:
            time.sleep(0.1)
            print("Sales Manager is busy")

class NoTalkProxy(Proxy):
    def talk(self):
        print("proxy checking for sales manager setting")
        time.sleep(0.1)
        print("This Sales Manager will not talk to you",
              "whether he/she is busy or not")

if __name__ == '__main__':
    p = Proxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()
    p = NoTalkProxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()
