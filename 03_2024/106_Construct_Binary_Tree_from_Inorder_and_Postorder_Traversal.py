# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TC == O(N^2) SC == (logN)
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)  # This one takes O(N) time, NOT COOL!!
        root.right = self.buildTree(inorder[idx + 1 :], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)
        return root


# TC == O(N) SC == O(N)
class SolutionV2:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        map_inorder = {}
        for i, val in enumerate(inorder):
            map_inorder[val] = i

        def recur(low, high):
            if low > high:
                return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid + 1, high)
            x.left = recur(low, mid - 1)
            return x

        return recur(0, len(inorder) - 1)
