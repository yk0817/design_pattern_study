import os
import sys
import tempfile
import numpy

def main():
    MathFactory

# abstarct factory
# エクセル読み込み
# テキストファイル作成
# テキストファイル書き込み

# 具体的にどのように区分けを行うか。
# ファイル形式によって変更を行う。
# xlsm、xls

class MathFactory:
    def make_file(Class,file_type):
        return Class.File(file_type)

    def make_calc(*arg):
        return Class.Calc(*args)



if __name__ == '__main__':
    main()
