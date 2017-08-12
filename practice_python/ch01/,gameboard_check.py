import io
import os
import sys
import tempfile

# 用途：gameboard.pyのメソッドを確認するために作成
def main():
    # checkers = CheckersBoard()
    # print(checkers.board)
    print(BlackChessRook())


class  AbstractBoard:
    
    def __init__(self,rows,columns):
        self.board = [[None for _ in range(columns)] for _ in range(rows)]
        self.populate_board()
    def populate_board(self):
        raise NotImplementedError
            
class CheckersBoard(AbstractBoard):
    def __init__(self):
        super().__init__(10,10)
    
    def populate_board(self):
        for x in range(0,9,2):
            for row in range(4):
                column = x + ((row + 1) % 2)

class Piece(str):
    __slots__ = ()

class BlackChessRook(Piece):

    __slots__ = ()

    def __new__(Class):
        print(Class)
        return super().__new__(Class, "\N{black draughts man}")
        
if __name__ == "__main__":
    main()