# TC == O(n^2) SC == O(1)
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(len(board)):
            checker = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for k in range(len(board[i])):
                if board[i][k].isdigit():
                    try:
                        checker.remove(board[i][k])
                    except ValueError:
                        return False
        for i in range(len(board)):
            checker = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for k in range(len(board[i])):
                if board[k][i].isdigit():
                    try:
                        checker.remove(board[k][i])
                    except ValueError:
                        return False
        for i in range(0, 3 * len(board), 3):
            checker = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            offset = i // 9 * 3
            k = 0
            if i >= 9:
                k = i // 9 * 3
                i %= 9
            for i in range(i, i + 3):
                k = offset
                for k in range(k, k + 3):
                    if board[i][k].isdigit():
                        try:
                            checker.remove(board[i][k])
                        except ValueError:
                            return False
        return True


# TC == O(n^2) SC == O(1) / Using string. More intuitive
class SolutionV2:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = []
        for i in range(len(board)):
            for k in range(len(board)):
                if board[i][k].isdecimal():
                    buf = "(" + board[i][k] + ")"
                    if (
                        buf + str(i) in seen
                        or str(k) + buf in seen
                        or str(k // 3) + buf + str(i // 3) in seen
                    ):
                        return False
                    else:
                        seen.append(buf + str(i))
                        seen.append(str(k) + buf)
                        seen.append(str(k // 3) + buf + str(i // 3))
        return True


potato = SolutionV2()
res = potato.isValidSudoku(
    board=[
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)
print(res)
