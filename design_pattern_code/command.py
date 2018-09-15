import abc
import time
import os

# csvファイル作成
# 行追加
# 行読み込み
# 行削除
# メソッドを簡単に追加出来る。

class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute():
        pass

class CreateFile(Command):
    def execute(self):
        cmd = "touch test.csv"
        os.system(cmd)

class InsertContent(Command):
    def execute(self):
        cmd = "date  >>test.csv"
        os.system(cmd)

        
class ReadContent(Command):
    def execute(self):
        cmd = "cat test.csv"
        os.system(cmd)

class DeleteFile(Command):
    def execute(self):
        # print("delte after... 2sec")
        time.sleep(2)
        cmd = "rm -rf test.csv"
        os.system(cmd)


def main():
    command_array = []
    command_array.append(CreateFile())
    command_array.append(InsertContent())
    command_array.append(ReadContent())
    command_array.append(DeleteFile())

    for cmd in command_array:
        cmd.execute()
    
if __name__ == '__main__':
    main()