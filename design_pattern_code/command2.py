import os
from os.path import lexists

class MoveFileCommand(object):
    
    def __init__(self,src,dest):
        self.src = src
        self.dest = dest
    
    def execute(self):
        self.rename(self.src,self.dest)
    
    def undo(self):
        self.rename(self.dest,self.src)
    
    def rename(self,src,dest):
        print("rename {} to {}".format(src,dest))
        os.rename(src,dest)
    
def main():
    command_stack = []
    
    command_stack.append(MoveFileCommand('foo.txt','bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt','baz.txt'))
    
    assert(not lexists("foo.txt"))
    assert(not lexists("bar.txt"))
    assert(not lexists("baz.txt"))
    try:
        with open("foo.txt","w"):
            pass
        for cmd in command_stack:
            cmd.execute()
        
        for cmd in reversed(command_stack):
            cmd.undo()
    finally:
        os.unlink("foo.txt")

if __name__ == '__main__':
    main()