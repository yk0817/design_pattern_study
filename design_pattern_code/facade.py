import time
# 参考
# https://github.com/faif/python-patterns/blob/master/structural/facade.py


class TC1:
    
    def run(self):
        print("test1")
        print("settup")
        print("finish")
        time.sleep(0.1)

class TC2:
    
    def run(self):
        print("test2")
        print("settup")
        print("finish")
        time.sleep(0.1)

        
class TC3:
    
    def run(self):
        print("test3")
        print("settup")
        print("finish")
        time.sleep(0.1)

class TestRunner:
    
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [self.tc1,self.tc2,self.tc3]
    
    def runAll(self):
        [i.run() for i in self.tests]

if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()