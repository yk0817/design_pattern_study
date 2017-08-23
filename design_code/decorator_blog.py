class PlainNumber():
    def __init__(self,num):
        self._num = num
    
    def render(self):
        return int(self._num)

class MultiplicationNumber(PlainNumber):
    def __init__(self,num):
        self._number = num
    
    def render(self,num):
        return self._number.render() * num

    
if __name__ == '__main__':
    plain_num = PlainNumber(11)
    multiple_output = MultiplicationNumber(plain_num)
    print("11*2=",multiple_output.render(2))
    

