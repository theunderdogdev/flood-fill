import random


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def print_mat(matrix):
    print(" ", *[i for i in range(0, 10)], sep="   ", end="  ")
    print(*[i for i in range(10, 20)], sep="  ")
    for i, row in enumerate(matrix):
        if i <= 9:
            print(i, end="   ")
        else:
            print(i, end="  ")
        for col in row:
            print(col, end="  ")
        print()

colors = [colored(0, 255, 0, 'G'), colored(255, 0, 0, 'R'), colored(255, 255, 0, 'Y'), colored(153, 51, 255, 'P')]
mat = []
v = 'R'

for _ in range(20):
    temp = []
    for i in range(20):
        v = random.randint(0, len(colors) - 1)
        temp.append(colors[v])
    mat.append(temp)



print_mat(mat)