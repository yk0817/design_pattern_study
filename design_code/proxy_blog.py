import abc

class Teacher(metaclass=abc.ABCMeta):
    def __init__(self):
        self.subject = "Math"
    
    @abc.abstractmethod
    def question_1(self):
        pass
        
    @abc.abstractmethod
    def question_2(self):
        pass
    

        
class MathTeacher(Teacher):
    def question_1(self,question):
        print(question,":は3です。")
        
    def question_2(self,question):
        EnglishTeacher().question_2(question)

class EnglishTeacher(Teacher):
    def question_1(self,question):
        MathTeacher().question_1(self,question)
    
    def question_2(self,question):
        print(question,"緑茶です。")

    
if __name__ == '__main__':
    # 生徒役
    MathTeacher().question_1("1+1は")
    MathTeacher().question_2("what does mean green tea?")