class Singleton:
    _instance = None
    
    # クラスインスタンス化した際、__new__→__init__が呼び出される。
    def __init__(self):
        print("init")
    
    def __new__(self):
        print("new")
        
        if self._instance is None:
            self._instance = super().__new__(self)
        
        return self._instance

if __name__ == '__main__':
    a = Singleton() #こんな感じで出力→<__main__.Singleton object at 0x106614438>
    b = Singleton() #↑と同じ。<__main__.Singleton object at 0x106614438>
    print(a)
    print(b)
    print(a is b)
