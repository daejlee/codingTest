import sys

mat = [[] for _ in range(9)]
for i in range(9):
    buf = sys.stdin.readline()
    for j in range(9):
        mat[i].append(int(buf[j]))


def check(x, y):
    # check row
    for i in range(9):
        buf = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        try:
            if mat[x][i] != 0:
                buf.remove(mat[x][i])
        except:
            return False
    # check col
    for i in range(9):
        buf = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        try:
            if mat[i][y] != 0:
                buf.remove(mat[i][y])
        except:
            return False
    # check square
    x_range = x // 3 * 3
    y_range = y // 3 * 3
    buf = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for curr_x in range(x_range, x_range + 3):
        for curr_y in range(y_range, y_range + 3):
            try:
                if mat[curr_x][curr_y] != 0:
                    buf.remove(mat[curr_x][curr_y])
            except:
                return False
    return True


def fill(x, y):
    for num in range(1, 10):
        mat[i][j] = num
        if check(x, y):
            return


for i in range(9):
    for j in range(9):
        if mat[i][j] == 0:
            fill(i, j)

for row in mat:
    print(row)
