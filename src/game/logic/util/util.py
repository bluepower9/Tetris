import time

WALL_KICKS = {
    (0,1): [(-1, 0), (-1, 1), (0, -2), (-1, -2)],
    (1,0): [(1, 0), (1,-1), (0, 2), (1, 2)],
    (1,2): [(1, 0), (1, -1), (0, 2), (1,2)],
    (2,1): [(-1,0), (-1, 1), (0, -2), (-1, -2)],
    (2,3): [(1, 0), (1, 1), (0, -2), (1, -2)],
    (3,2): [(-1, 0), (-1, -1), (0, 2), (-1, 2)],
    (3,0): [(-1, 0), (-1, -1), (0, 2), (-1, 2)],
    (0,3): [(1, 0), (1, 1), (0, -2), (1, -2)]
}

WALL_KICKS_I = {
    (0,1): [(-2, 0), (1, 0), (-2, -1), (1, 2)],
    (1,0): [(2, 0), (-1, 0), (2, 1), (-1, -2)],
    (1,2): [(-1, 0), (2, 0), (-1, 2), (2, -1)],
    (2,1): [(1, 0), (-2, 0), (1, -2), (-2, 1)],
    (2,3): [(2, 0), (-1, 0), (2, 1), (-1, -2)],
    (3,2): [(-2, 0), (1, 0), (-2, -1), (1, 2)],
    (3,0): [(1, 0), (-2, 0), (1, -2), (-2, 1)],
    (0,3): [(-1, 0), (2, 0), (-1, 2), (2, -1)]
}

SCORING = {
    '0': 0,
    '1': 100,
    '2': 300,
    '3': 500,
    'tetris': 800
}