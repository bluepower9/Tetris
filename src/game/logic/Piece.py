from copy import deepcopy, copy
from util import WALL_KICKS, WALL_KICKS_I

TETROMINOES = {
    0: {
        'T': [(-2, 0), (-1, 0), (-1,-1), (0, 0)],
        'O': [(-1, -1), (0, -1), (-1, 0), (0, 0)],
        'J': [(-2, -1), (-2, 0), (-1, 0), (0,0)],
        'L': [(-2, 0), (-1, 0), (0, 0), (0, -1)],
        'I': [(-2, -1), (-1, -1), (0, -1), (1, -1)],
        'S': [(-2, 0), (-1, 0), (-1, -1), (0, -1)],
        'Z': [(-2, -1), (-1, -1), (-1, 0), (0, 0)]
    },
    1: {
        'T': [(-1, -1), (-1, 0), (0, 0), (-1, 1)],
        'O': [(-1, -1), (0, -1), (-1, 0), (0, 0)],
        'J': [(-1,-1), (0, -1), (-1, 0), (-1, 1)],
        'L': [(-1, -1), (-1, 0), (-1, 1), (0, 1)],
        'I': [(0, -2), (0, -1), (0, 0), (0, 1)],
        'S': [(-1, -1), (-1, 0), (0, 0), (0, 1)],
        'Z': [(0, -1), (0, 0), (-1, 0), (-1, 1)]
    },
    2: {
        'T': [(-2, 0), (-1, 0), (0, 0), (-1, 1)],
        'O': [(-1, -1), (0, -1), (-1, 0), (0, 0)],
        'J': [(-2, 0), (-1, 0), (0, 0), (0, 1)],
        'L': [(-2, 0), (-1, 0), (0, 0), (-2, 1)],
        'I': [(-2, 0), (-1, 0), (0, 0), (1, 0)],
        'S': [(-1, 0), (0, 0), (-2, 1), (-1, 1)],
        'Z': [(-2, 0), (-1, 0), (-1, 1), (0, 1)]
    },
    3: {
        'T': [(-1, -1), (-1, 0), (-2, 0), (-1, 1)],
        'O': [(-1, -1), (0, -1), (-1, 0), (0, 0)],
        'J': [(-1,-1), (-2, 1), (-1, 0), (-1, 1)],
        'L': [(-1, -1), (-1, 0), (-1, 1), (-2, -1)],
        'I': [(-1, -2), (-1, -1), (-1, 0), (-1, 1)],
        'S': [(-2, -1), (-2, 0), (-1, 0), (-1, 1)],
        'Z': [(-1, -1), (-2, 0), (-1, 0), (-2, 1)]
    }
}


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getpixel(self):
        return self.x, self.y
    
    def __str__(self) -> str:
        return str((self.x, self.y))


class Piece:
    def __init__(self, piece, x=5, y=1, rotation=0):
        self.name = piece
        self.center = [x, y]
        #self.piece = [Block(bx+x, by+y) for bx, by in TETROMINOES[piece]]
        self.rotation = rotation   # spawn state = 0. goes up to 3 going around clockwise rotations


    @property
    def piece(self):
        return self.get_blocks()

    def get_blocks(self):
        coords = TETROMINOES[self.rotation][self.name]
        dx, dy = self.center
        
        return [(x+dx, y+dy) for x, y in coords]


    def srs_kick(self, rotation:tuple, board) -> list:
        '''
        performs kick test and returns new coords if it kicks piece. Else returns (None, None).
        Also updates the coords and resets rotation if invalid rotation.
        '''
        coord = copy(self.center)
        if self.name == 'I':
            kicks = WALL_KICKS_I[rotation]
        else:
            kicks = WALL_KICKS[rotation]
        
        for dx, dy in kicks:
            self.center[0] += dx
            self.center[1] -= dy    # kick table has y inversed so positive values means move up.

            valid = True
            # print('test: ', (dx, dy), ' piece: ', self.piece)
            for block in self.piece:
                if self.has_collision(block, board):
                    valid = False
            if valid:
                return self.center
            
            self.center = copy(coord) # resets center and continues to next test
        
        self.rotation = rotation[0]
        # print('failed srs. orig: ', coord, ' current: ', self.center, 'rotation: ', rotation, 'current rot: ', self.rotation)
        return None, None



    def has_collision(self, coord, board):
        '''
        Checks if a block collides with anything including wall and floor
        '''
        x, y = coord
        if x >= len(board[0]) or x < 0 or y >= len(board) or board[y][x] == 1:
            return True

        return False
            

    def rotate_clockwise(self, board):
        start_rotation = self.rotation
        self.rotation = (self.rotation + 1) % 4
        for x,y in self.piece:
            if self.has_collision((x,y), board):
                self.srs_kick((start_rotation, self.rotation), board)
                break
    

    def rotate_counterclockwise(self, board):
        start_rotation = self.rotation
        self.rotation -= 1
        if self.rotation < 0:
            self.rotation = 3

        for x,y in self.piece:
            if self.has_collision((x,y), board):
                self.srs_kick((start_rotation, self.rotation), board)
                break


    def move_down(self, board):
        tempy = self.center[1]
        self.center[1] += 1

        for x, y in self.piece:
            if self.has_collision((x, y), board):
                self.center[1] = tempy
                return False
        
        return True
        
       

    def move_horizontal(self, dx, board):
        tempx = self.center[0]
        self.center[0] += dx

        for x, y in self.piece:
            if self.has_collision((x, y), board):
                self.center[0] = tempx
                return False

        return True



    


    

