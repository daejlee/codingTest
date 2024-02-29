from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TC == O(N), SC == O(logN), if it's balanced tree / DFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        self.rightView(root, res, 0)
        return res

    def rightView(self, curr: TreeNode, res: list[int], currDepth: int):
        if curr == None:
            return
        if currDepth == len(res):
            res.append(curr.val)
        self.rightView(curr.right, res, currDepth + 1)
        self.rightView(curr.left, res, currDepth + 1)


# TC == O(N), SC == O(N) / BFS
class SolutionV2:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root == None:
            return []
        q = Queue()
        q.put(root)
        res = []
        while q.empty() == False:
            size = q.qsize()
            while size > 0:
                size -= 1
                curr = q.get()
                if size == 0:
                    res.append(curr.val)
                if curr.left != None:
                    q.put(curr.left)
                if curr.right != None:
                    q.put(curr.right)
        return res
