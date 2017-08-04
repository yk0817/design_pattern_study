import sys
import openpyxl
import glob
import xlrd
import re
from abc import ABCMeta, abstractmethod

# 抽象メソッド
class ExcelFactory(metaclass=ABCMeta):
    # デコレータをつけると、サブクラスはオーバーライドしないとエラーになる。
    @abstractmethod
    def read_file():
        pass

class XlsRead(ExcelFactory):
    def __init__(self,file):
        self.__file_name = file
        print(self.__file_name + "の読み取りを行います。")

    def read_file(self,worksheet):
        books = openpyxl.load_workbook(worksheet)

class MxlsRead(ExcelFactory):
    def __init__(self,file):
        self.__file_name = file
        print(self.__file_name + "の読み取りを行います。")

    def read_file(self,worksheet):
        books = xlrd.open_workbook(worksheet)
        print(books.sheet_buy_index(1).cell_value(rowx=0,colx=0))

def main():
    # インスタンス作成
    xls_instance = XlsRead()
    mxls_instance = MxlsRead()
    # 実行ファイル元にエクセルファイルがあると想定
    worksheets = glob.glob('./*')

    for worksheet in worksheets:
        if re.match(r"\.xls$",worksheet):
            xls_instance.read_file(worksheet)
        elif re.match(r"\.xlsm$",worsheet):
            mxls_instance.read_file(worksheet)


if __name__ == '__main__':
    main()
