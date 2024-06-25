# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TC == O(N) SC == O(N)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_blueprint = []
        self.search(p, p_blueprint)
        q_blueprint = []
        self.search(q, q_blueprint)
        return p_blueprint == q_blueprint

    def search(self, root: [TreeNode], blueprint: list[int]):
        if root == None:
            blueprint.append(None)
            return
        else:
            blueprint.append(root.val)
        self.search(root.left, blueprint)
        self.search(root.right, blueprint)


# TC == O(N) SC == O(N) or O(logn) if balanced
class SolutionV2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        return p is q
