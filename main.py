# 8 block puzzle solver using Heuristic Search
import math
import copy

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
g = [
    [2, 0, 3],
    [1, 4, 5],
    [7, 8, 6]
]


def get_inv_count(arr):
    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


# This function returns true
# if given 8 puzzle is solvable.
def is_solvable(puzzle):
    # Count inversions in given 8 puzzle
    inv_count = get_inv_count([j for sub in puzzle for j in sub])

    # return true if inversion count is even.
    return inv_count % 2 == 0


# Driver code

if is_solvable(g):
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
        # print(moves, row, col)
        for m in ["l", "r", "u", "d"]:
            r = row
            c = col
            temp = copy.deepcopy(a)
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
                if c != col and row == r:
                    # print(temp[row][c], temp[row][col])
                    temp[row][c], temp[row][col] = temp[row][col], temp[row][c]
                    # print(f"Executed col{c}<->col{col} in row{row}")
                elif r != row and col == c:
                    # print(temp[r][col], temp[row][col])
                    temp[r][col], temp[row][col] = temp[row][col], temp[r][col]
                    # print(f"Executed row{r}<->row{row} in col{col}")
                # print_puzzle(temp)
                calc_heuristic_val(temp, m)
                # print(moved_cost)
        final_move(row, col)


    def final_move(row, col):
        r = row
        c = col
        min_cost = min(moved_cost, key=moved_cost.get)
        if min_cost == "l":
            c = col - 1
        elif min_cost == "u":
            r = row - 1
        elif min_cost == "r":
            c = col + 1
        else:
            r = row + 1
        if c != col and row == r:
            a[row][c], a[row][col] = a[row][col], a[row][c]
        elif r != row and col == c:
            a[r][col], a[row][col] = a[row][col], a[r][col]
        heuristic_costs.append(moved_cost[min_cost])


    while a != g:
        check_moves()
        print_puzzle(a)
        print("*" * 10)

    print(heuristic_costs)
else:
    print("Not Solvable")

