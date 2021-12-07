from collections import deque
import random

# Below lists detail all eight possible movements
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


# Takes rgb values of the color and text that is to be colored returns an ansi escape sequence for the color
def colored(rd, gn, bl, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(rd, gn, bl, text)


# prints the matrix whenever called
# takes two args one the matrix and other is number of columns
# For print formatting it checks if the number of columns are 1 digit or two digit numbers
# if they are two digit numbers it decreases formatting delimiter by one else it uses the usual "3 delimits"
def print_mat(matrix, columns):
    if columns < 9:
        print(" ", *[j for j in range(0, columns)], sep="   ", end="  ")
    else:
        print(" ", *[j for j in range(0, 10)], sep="   ", end="  ")
    if columns > 10:
        print(*[j for j in range(10, columns)], sep="  ")
    else:
        print()
    for k, rows in enumerate(matrix):
        if k <= 9:
            print(k, end="   ")
        else:
            print(k, end="  ")
        for cols in rows:
            print(cols, end="  ")
        print()
# check if it is possible to go to pixel (x, y) from the
# current pixel. The function returns false if the pixel
# has a different color, or it's not a valid pixel


def is_safe(mat, x, y, target):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == target


# Flood fill using BFS
def flood_fill(mat, x, y, replacement):
    # base case
    if not mat or not len(mat):
        return

    # create a queue and enqueue starting pixel
    q = deque()
    q.append((x, y))

    # get the target color
    target = mat[x][y]

    # target color is same as replacement
    if target == replacement:
        return

    # break when the queue becomes empty
    while q:

        # dequeue front node and process it
        x, y = q.popleft()

        # replace the current pixel color with that of replacement
        mat[x][y] = replacement

        # process all eight adjacent pixels of the current pixel and
        # enqueue each valid pixel
        for k in range(len(row)):
            # if the adjacent pixel at position (x + row[k], y + col[k]) is
            # is valid and has the same color as the current pixel
            if is_safe(mat, x + row[k], y + col[k], target):
                # enqueue adjacent pixel
                q.append((x + row[k], y + col[k]))


if __name__ == '__main__':
    # matrix showing portion of the screen having different colors
    rs = int(input("Enter Number of rows: "))
    cs = int(input("Enter Number of cols: "))
    colors = [colored(0, 255, 0, 'G'), colored(255, 0, 0, 'R'), colored(255, 255, 0, 'Y'), colored(153, 51, 255, 'P')]
    gen_mat = []
    v = None
    for _ in range(rs):
        temp = []
        for i in range(cs):
            v = random.randint(0, len(colors) - 1)
            temp.append(colors[v])
        gen_mat.append(temp)
    yes = 'y'
    while yes == 'y':
        print_mat(gen_mat, cs)
        r = int(input("Enter row number: "))
        c = int(input("Enter col number: "))
        replaced = colored(153, 255, 255, 'C')
        flood_fill(gen_mat, r, c, replaced)
        print_mat(gen_mat, cs)
        yes = input("Do you want to flood fill the matrix again (y/n):").lower()
    # print the colors after replacement
