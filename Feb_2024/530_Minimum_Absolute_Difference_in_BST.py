# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TC == O(N) SC == O(logN)
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float("inf")
        self.traverse(root)
        return self.min_diff

    def traverse(self, node: TreeNode):
        if node is None:
            return
        self.traverse(node.left)
        if self.prev is not None:
            self.min_diff = min(self.min_diff, node.val - self.prev)
        self.prev = node.val
        self.traverse(node.right)
