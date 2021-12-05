from collections import deque

# Below lists detail all eight possible movements
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


# check if it is possible to go to pixel (x, y) from the
# current pixel. The function returns false if the pixel
# has a different color, or it's not a valid pixel
def isSafe(mat, x, y, target):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == target


# Flood fill using BFS
def floodfill(mat, x, y, replacement):
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
            if isSafe(mat, x + row[k], y + col[k], target):
                # enqueue adjacent pixel
                q.append((x + row[k], y + col[k]))


if __name__ == '__main__':
    # matrix showing portion of the screen having different colors
    import random

    colors = ['Y', 'R', 'B', 'G']
    mat = []
    v = 'R'
    for _ in range(7):
        temp = []
        for i in range(7):
            v = random.randint(0, len(colors) - 1)
            temp.append(colors[v])
        mat.append(temp)

    # start node

    for i in mat:
        print(i)
    print('-----'*10)
    # having target color `X`
    # replacement color
    r = int(input("Enter x of pixels"))
    c = int(input("Enter y of pixels"))
    replacement = 'C'
    floodfill(mat, r, c, replacement)

    # print the colors after replacement
    for r in mat:
        print(r)
