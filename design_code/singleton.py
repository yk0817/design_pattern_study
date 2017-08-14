class Singleton:
    initial_instance_name = None
    
    # クラスインスタンス化した際、__new__→__init__が呼び出される。
    def __init__(self):
        print("init")
    
    def __new__(self):
        print("new")
        
        if self.initial_instance_name is None:
            self.initial_instance_name = super().__new__(self)
        
        return self.initial_instance_name

if __name__ == '__main__':
    a = Singleton() #こんな感じで出力→<__main__.Singleton object at 0x106614438>
    b = Singleton() #↑と同じ。<__main__.Singleton object at 0x106614438>
    print(a)
    print(b)
    print(a is b)
