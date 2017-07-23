import abc
import click

# 抽象クラス
# 抽象メソッド
# abstract 

# metaclass クラスを定義する際に用いるクラス
# インスタンス化
# 抽象クラスをサブクラス化するので抽象クラスを用いることが出来る。
class AbstractTaxCalcBuilder(metaclass=abc.ABCMeta)
    # 抽象メソッドはデコレータで就職する
    @abc.abstractmethod
    def add_tax(self,rate1):
        pass
    
    @abc.abstractmethod
    def minus_tax(self,rate2):
        pass
        
    @abc.abstractmethod
    def message_tax(self,message):
        pass
    
class ConsumptionTaxBuilder(AbstractTaxCalcBuilder):
    super().add_tax()

class DeductionTaxBuilder(AbstractTaxCalcBuilder):
    
        

if __name__ == '__main__':
    main()    