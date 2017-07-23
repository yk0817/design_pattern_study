import abc
import click

# 抽象クラス
# 抽象メソッド
# abstract 
# metaclass クラスを定義する際に用いるクラス
# インスタンス化
# 抽象クラスをサブクラス化するので抽象クラスを用いることが出来る。
class AbstractTaxCalcBuilder(metaclass=abc.ABCMeta):
    # 抽象メソッドはデコレータで就職する
    @abc.abstractmethod
    def calc_tax(self,rate):
        pass
        
    @abc.abstractmethod
    def message_tax(self,message):
        pass
    
class ConsumptionTaxBuilder(AbstractTaxCalcBuilder):
    def __init__(self):
        self.rate = 0
        self.message = ""
        
    def set_total(self,total):
        self.total = total
        
    def calc_tax(self,rate):
        self.rate = rate
    
    def message_tax(self):
        tax = self.total * self.rate
        message = " ".join(["あなたの払う税金は",str(tax),"円です"])
        print(message)

def main():
    tax = ConsumptionTaxBuilder()
    tax.set_total(1000)
    tax.calc_tax(0.3)
    tax.message_tax()
    
if __name__ == '__main__':
    main()    