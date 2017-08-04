import sys
import openpyxl
import glob
import xlrd
import re
from abc import ABCMeta, abstractmethod

# 抽象メソッド
class AbstExcelFactory(metaclass=ABCMeta):
    # デコレータをつけると、サブクラスはオーバーライドしないとエラーになる。
    @abstractmethod
    def read_file():
        pass

class XlsRead(AbstExcelFactory):
    def __init__(self,file):
        self.__file_name = file
        print(self.__file_name + "の読み取りを行います。")

    def read_file(arg):
        pass


class MxlsRead(AbstExcelFactory):
    def __init__(self,file):
        self.__file_name = file
        print(self.__file_name + "の読み取りを行います。")

    def read_file(arg):
        pass

def main():
    # インスタンス作成
    xls_instance = XlsRead()
    mxls_instance = MxlsRead()
    worksheets = glob.glob('./*')

    for worksheet in worksheets:
        if re.match(r"\.xls$",worksheet):

        elif re.match(r"\.xlsm$",worsheet):

        else:
            pass


if __name__ == '__main__':
    main()
