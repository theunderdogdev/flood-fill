# 8 block puzzle solver using Heuristic Search
import math

a = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]
g = [
    [1, 2, 3],
    [4, 5, 0],
    [6, 7, 8]
]

heuristic_costs = []


def print_puzzle(work_arr):
    print(*work_arr[0:3], sep="\n")


moved_cost = {'l': math.inf, 'r': math.inf, 'u': math.inf, 'd': math.inf}


def calc_heuristic_val(work_arr, dir_key):
    heur_val = 0
    for i in range(3):
        for j in range(3):
            if work_arr[i][j] != g[i][j]:
                heur_val += 1
    moved_cost[dir_key] = heur_val


def predict_moves():
    poss_move = []
    r, c = None, None
    for i, row in enumerate(a):
        if 0 in row:
            c = row.index(0)
            r = i
    shift_val = None
    for move in ["l", "r", "u", "d"]:
        if move == "l":
            shift_val = c - 1
        elif move == "u":
            shift_val = r - 1
        elif move == "r":
            shift_val = c + 1
        else:
            shift_val = r + 1
        if 0 <= shift_val < 3:
            poss_move.append(move)
    return poss_move, r, c


def check_moves():
    moves, row, col = predict_moves()
    r = row
    c = col
    print(moves,row,col)
    for m in ["l", "r", "u", "d"]:
        temp = a.copy()
        if m not in moves:
            moved_cost[m] = math.inf
        else:
            if m == "l":
                c = col - 1
            elif m == "u":
                r = row - 1
            elif m == "r":
                c = col + 1
            else:
                r = row + 1
            if c != col:
                temp[row][c], temp[row][col] = temp[row][col], temp[row][c]
            else:
                temp[r][col], temp[row][col] = temp[row][col], temp[r][col]
            calc_heuristic_val(temp, m)
            print_puzzle(temp)
            print(moved_cost)


check_moves()
