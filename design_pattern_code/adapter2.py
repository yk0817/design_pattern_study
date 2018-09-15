import abc
import os
import csv

class Format:
    def __init__(self,content):
        self.__content = content
    
    def make_file_csv(self,file_name):
        f = open('{}.csv'.format(file_name),'w')
        f.write(self.__content)
    
    def make_file_txt(self,file_name):
        f = open('{}.txt'.format(file_name),'w')
        f.write(self.__content)


class TextMake(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make_csv(self):
        pass
    
    @abc.abstractmethod
    def make_txt(self):
        pass

class TextMakeFormat(TextMake,Format):
    def __init__(self,content):
        super().__init__(content)
    
    def make_csv(self,file_name):
        self.make_file_csv(file_name)
    
    def make_txt(self,file_name):
        self.make_file_txt(file_name)


if __name__ == '__main__':
    textobj = TextMakeFormat('おはようございます。\n今日も元気で頑張りましょう。')
    textobj.make_csv("csv_file")
    textobj.make_txt("txt_file")