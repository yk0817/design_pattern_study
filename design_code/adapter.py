import abc


class Banner:
    def __init__(self, string):
        self.__string = string

    def show_with_paren(self):
        print('({})'.format(self.__string))

    def show_with_aster(self):
        print('({0})'.format(self.__string))


class Printer(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def print_weak(self):
      pass

  @abc.abstractmethod      
  def print_strong(self):
      pass


class PrinterBanner(Printer,Banner):

    def __init__(self, string):
        super().__init__(string)

    def print_weak(self):
        self.show_with_paren()
    
    def print_strong(self):
        self.show_with_aster()


if __name__ == '__main__':
    pb = PrinterBanner('Bye')
    pb.print_weak() 
    pb.print_strong()