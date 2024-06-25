import sys as s


# 1st row - 1
# 2nd row - 2
# 3rd row - 4
# 4th row - 6
# ...
# nth row - 2 * (n - 1)
# We needed multi dimensional DP !!!!! now, memo is 1d


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        memo = [s.maxsize] * n
        idx_memo = [0] * n
        memo[0] = triangle[0][0]
        idx_memo[0] = triangle[0][0]
        self.search(1, 0, memo, idx_memo, triangle)
        self.search(1, 1, memo, idx_memo, triangle)
        print(memo)
        print(idx_memo)
        return sum(idx_memo)

    def search(
        self,
        row: int,
        col: int,
        memo: list[int],
        idx_memo: list[int],
        tri: list[list[int]],
    ):
        if row >= len(tri) or col >= len(tri[row]) - 1:
            return
        if (
            tri[row][col] > tri[row][col + 1]
            and memo[row] > memo[row - 1] + tri[row][col + 1]
        ):
            memo[row] = memo[row - 1] + tri[row][col + 1]
            idx_memo[row] = tri[row][col + 1]
        if col >= len(tri[row]):
            return
        if (
            tri[row][col + 1] > tri[row][col]
            and memo[row] > memo[row - 1] + tri[row][col]
        ):
            memo[row] = memo[row - 1] + tri[row][col]
            idx_memo[row] = tri[row][col]
        self.search(row + 1, col, memo, idx_memo, tri)
        self.search(row + 1, col + 1, memo, idx_memo, tri)


# Solution - Iteration TC == O(N) SC == O(N^2)
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if not triangle:
            return 0

        memo = [[0] * len(row) for row in triangle]  # Make 2d memo
        memo[0][0] = triangle[0][0]

        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                if col == 0:  # Far left
                    memo[row][col] = memo[row - 1][col] + triangle[row][col]
                elif col == len(triangle[row]) - 1:  # Far right
                    memo[row][col] = memo[row - 1][col - 1] + triangle[row][col]
                else:  # Between
                    memo[row][col] = (
                        min(memo[row - 1][col - 1], memo[row - 1][col])
                        + triangle[row][col]
                    )

        return min(memo[-1])  # Return smallest from last row


# Solution - Iteration TC == O(N) SC == O(N)
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        minlen = triangle[-1].copy()  # 마지막 행으로 minlen 초기화
        for layer in range(n - 2, -1, -1):  # 바텀업 방식으로 각 레이어를 순회
            for i in range(layer + 1):  # 각 레이어의 노드를 순회
                # 현재 노드에서 가능한 두 자식 중 최소값을 찾아 현재 노드의 값과 더함
                minlen[i] = min(minlen[i], minlen[i + 1]) + triangle[layer][i]
        return minlen[0]  # 최상단 노드의 최소 경로 합 반환
