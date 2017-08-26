from abc import *

# csvファイル作成
# 行追加
# 行読み込み
# 行削除
# メソッドを簡単に追加出来る。

class Command(metaclass=abc.ABCMeta):
    def __init__(self,file_type):
        self.file_type = file_type
        
    @abc.abstractmethod
    def execute():
        pass

class CreateFile(Command):
    def execute():
        pass

class InsertContent(Command):
    def execute():
        pass
        
class ReadContent(Command):
    def execute():
        pass

class DeleteFile(Command):
    def execute():
        pass

def main():
    
        
if __name__ == '__main__':
    main()