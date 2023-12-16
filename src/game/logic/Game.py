from Board import Board
from Piece import Piece, TETROMINOES
import random
import time
import os

class Game:
    def __init__(self, tickrate = 60):
        self.tickrate = tickrate
        self.board = Board()
        self.piece = self.get_random_piece()
        self.piece = Piece('I', rotation=1)
        self.score = 0

        self.ticks = 0
        self.drop_time = 250
        self.drop_ticks = round(self.tickrate/(1000/self.drop_time))

        self.moved_down = True
        self.lock_delay = 500
        self.lock_ticks = round(self.tickrate/(1000/self.lock_delay))
        self.lock_ticks_count = 0   # number of ticks that the piece has not moved down
        
    
    def get_random_piece(self):
        return Piece(random.choice(list(TETROMINOES[0].keys())))


    def update(self):
        # moves piece down after set delay. 
        # resets move down counter if the piece moves down used to lock piece
        if self.ticks%self.drop_ticks == 0:
            #random moves for testing
            move_dir = random.choice([-1,0,1])
            self.piece.move_horizontal(move_dir, self.board.state())
            rand_turn = random.random()
            # rand_turn = .8
            if rand_turn < .3:
                self.piece.rotate_counterclockwise(self.board.state())
            elif rand_turn < .6:
                self.piece.rotate_clockwise(self.board.state())
            
            self.moved_down = self.piece.move_down(self.board.state())
            if self.moved_down:
                self.lock_ticks_count = 0
            
        # checks if piece needs to be locked.
        lockpiece = False
        if self.lock_ticks_count == self.lock_ticks:
            lockpiece=True
            self.lock_ticks_count = 0

        gameover = self.board.update(self.piece, lockpiece=lockpiece)

        if lockpiece:
            self.piece = self.get_random_piece()
            self.moved_down = True

        self.ticks += 1
        if not self.moved_down:
            self.lock_ticks_count += 1
            
        # handles tick rate. currently max tick rate is about 40? due to time.sleep precision
        time.sleep(1/self.tickrate)
  

        return gameover



    def play(self, cli=True):
        print(self.board)

        #testing for tetris
        # self.board.board[-1] = [1 for i in range(9)] + [0]
        # self.board.board[-2] = [1 for i in range(9)] + [0]
        # self.board.board[-3] = [1 for i in range(9)] + [0]
        # self.board.board[-4] = [1 for i in range(9)] + [0]
        
        gameover = False
        while not gameover:
            gameover, points = self.update()
            self.score += points
            if cli:
                os.system('cls')
                print(self.board)
                print(f'Score: {self.score}')
                # print(self.board.height)


if __name__ == '__main__':
    game = Game()
    game.play()