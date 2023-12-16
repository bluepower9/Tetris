from Piece import Piece, TETROMINOES
import random
import time
from util import SCORING


class Board:
    def __init__(self, rows=20, cols=10, spawnzone=1) -> None:
        self.spawnzone = spawnzone
        self.size = rows, cols # row x col
        self.board = [[0 for i in range(cols)] for i in range(rows+spawnzone)]
        self.height = 0
     
    def clear_piece(self):
        # removes original piece
        for row in self.board:
            for c in range(len(row)):
                if row[c] == 2:
                    row[c] = 0


    def draw_piece(self, piece: Piece):
        self.clear_piece()

        #draws new position
        for col, row in piece.piece:
            # print(row, col)
            self.board[row][col] = 2


    def lock_piece(self, piece):
        '''
        locks the piece on the board and returns the rows that the piece occupies.
        updates the max height of the stack.
        '''
        self.clear_piece()
        result = []         # rows the piece occupies
        for col, row in piece.piece:
            # print(row, col)
            self.board[row][col] = 1
            height = self.size[0]+self.spawnzone - row
            result.append(row)
            if height > self.height:
                self.height = height

        return result


    def clear_rows(self, rows:list) -> int:
        '''
        takes in a list of the rows to check if they should be cleared.
        returns the calculated score for clearing the rows. 
        '''
        num_cleared = 0
        for row in rows:
            if 0 not in self.board[row]:
                self.board.pop(row)
                self.board.insert(0, [0 for i in range(self.size[1])])
                num_cleared += 1
        
        action = str(num_cleared)
        if num_cleared == 4:
            action = 'tetris'

        return SCORING[action]



    def update(self, piece:Piece, lockpiece=False) -> bool:
        '''
        updates the board with the given piece position and locks the piece in place if required.
        returns if true if gameover else False
        '''
        points = 0
        if lockpiece:
            rows = self.lock_piece(piece)
            points = self.clear_rows(rows)
        else:
            self.draw_piece(piece)

        return self.height > self.size[0], points


    def state(self):
        return self.board

    def __str__(self) -> str:
        result = ''
        for row in self.board:
            for c in row:
                if c:
                    result += str(c) + ' '
                else:
                    result += '. '
            result += '\n'
        
        return result


if __name__ == '__main__':
    board = Board()

    print(board)