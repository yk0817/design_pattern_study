import os
import sys
import tempfile
import numpy

# tempfileをファイルに書き込み
# overrideを作成
# 消費税との掛け算を考えるか〜

class MathFactory:
    def make_file(Class,file_type):
        return Class.File(file_type)
    
    def make_calc(arg):
        return Class.Calc
    




if __name__ == '__main__':
    main()