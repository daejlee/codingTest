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


potato = Solution()
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
