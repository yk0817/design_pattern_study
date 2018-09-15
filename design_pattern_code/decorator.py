# https://github.com/faif/python-patterns/blob/master/structural/decorator.py


class TextTag():
    def __init__(self,text):
        self._text = text
    
    def render(self):
        return self._text


class BoldWrapper(TextTag):
    def __init__(self,wrapped):
        self._wrapped = wrapped
    
    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())

class ItalicWrapper(TextTag):
    def __init__(self,wrapped):
        self._wrapped = wrapped
    
    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())

if __name__ == '__main__':
    simple_hello = TextTag("hello,world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print("before:",special_hello.render())
    print("after:",simple_hello.render())