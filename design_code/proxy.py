import time
<<<<<<< HEAD
# 参考
# https://github.com/faif/python-patterns/blob/master/structural/proxy.py

class SalesManager:
    def talk(self):
        print("sales manager ready to talk")
=======


class SalesManager:
    def talk(self):
        print("Sales Manager ready to talk")

>>>>>>> 5b59aa2eda786e5416523e5dca6561959e14755a

class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def talk(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
<<<<<<< HEAD
            self.safes = SalesManager()
            time.sleep(0.1)
            self.safes.talk()
=======
            self.sales = SalesManager()
            time.sleep(0.1)
            self.sales.talk()
>>>>>>> 5b59aa2eda786e5416523e5dca6561959e14755a
        else:
            time.sleep(0.1)
            print("Sales Manager is busy")

<<<<<<< HEAD
class NoTalkProxy(Proxy):
    def talk(self):
        print("proxy checking for sales manager setting")
=======

class NoTalkProxy(Proxy):
    def talk(self):
        print("Proxy checking for Sales Manager availability")
>>>>>>> 5b59aa2eda786e5416523e5dca6561959e14755a
        time.sleep(0.1)
        print("This Sales Manager will not talk to you",
              "whether he/she is busy or not")

<<<<<<< HEAD
=======

>>>>>>> 5b59aa2eda786e5416523e5dca6561959e14755a
if __name__ == '__main__':
    p = Proxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()
    p = NoTalkProxy()
    p.talk()
    p.busy = 'Yes'
<<<<<<< HEAD
    p.talk()
=======
    p.talk()
>>>>>>> 5b59aa2eda786e5416523e5dca6561959e14755a
