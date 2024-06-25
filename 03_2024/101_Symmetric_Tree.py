from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TC == O(N) SC == O(N)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        dq = deque()
        dq.append(root)
        while len(dq):
            level = []
            while len(dq):
                level.append(dq.popleft())
            for i in range(len(level)):
                if level[i] == None or level[-i - 1] == None:
                    if level[i] == level[-i - 1] == None:
                        continue
                    return False
                if level[i].val != level[-i - 1].val:
                    return False
                if level[i].left:
                    dq.append(level[i].left)
                else:
                    dq.append(None)
                if level[i].right:
                    dq.append(level[i].right)
                else:
                    dq.append(None)
        return True


# TC == O(N) SC == O(logN) ~ O(N)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.search(root.left, root.right)

    def search(self, left: TreeNode, right: TreeNode):
        if left == None or right == None:
            return left == right
        if left.val != right.val:
            return False
        return self.search(left.right, right.left) and self.search(
            left.left, right.right
        )
