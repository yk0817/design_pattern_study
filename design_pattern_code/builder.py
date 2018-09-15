import abc

class TaxCalcDirector():
    def __init__(self, builder):
        self.__builder = builder
        
    def construct(self,total,tax):
        self.__builder.set_total(self,total)
        self.__builder.set_tax(self,tax)
        self.__builder.message_tax(self)

class AbstractTaxCalcBuilder(metaclass=abc.ABCMeta):
    # 抽象メソッドはデコレータで継承する
    @abc.abstractmethod
    def set_total(self,total):
        pass

    @abc.abstractmethod
    def set_tax(self,rate):
        pass
        
    @abc.abstractmethod
    def message_tax(self,message):
        pass
    
class ConsumptionTaxBuilder(AbstractTaxCalcBuilder):
    def __init__(self):
        self.rate = 0
        self.total = 0
        
    def set_total(self,total):
        self.total = total
        
    def set_tax(self,rate):
        self.rate = rate
    
    def message_tax(self):
        tax = self.total * self.rate
        message = " ".join(["あなたの払う税金は",str(tax),"円です"])
        print(message)
        
class DeductionTaxBuilder(AbstractTaxCalcBuilder):
    def __init__(self):
        self.rate = 0
        self.total = 0
        
    def set_total(self,total):
        self.total = total
        
    def set_tax(self,rate):
        self.rate = -1 * rate
    
    def message_tax(self):
        tax = self.total * self.rate
        message = " ".join(["あなたが還付される税金は",str(tax),"円です"])
        print(message)

def main():
    # 支払う税金
    tax = TaxCalcDirector(ConsumptionTaxBuilder)
    tax.construct(1000,0.3)
    # 還付
    tax = TaxCalcDirector(DeductionTaxBuilder)
    tax.construct(200,0.1)

    
if __name__ == '__main__':
    main()    
