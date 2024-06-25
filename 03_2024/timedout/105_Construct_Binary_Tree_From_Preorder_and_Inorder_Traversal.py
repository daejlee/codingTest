# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# I had the idea of dividing area with idx, but failed to finish. We needed to RECUR the sh*t out of this
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        n = len(preorder)
        memo = [preorder[0]]
        res = TreeNode(val=preorder[0], left=None, right=None)
        root = res
        parent = None
        for i in range(1, n):
            val = preorder[i]
            idx = inorder.index(val)
            if idx == 0:
                l = None
                r = inorder[1]
            elif idx == n - 1:
                l = inorder[idx - 1]
                r = None
            else:
                l = inorder[idx - 1]
                r = inorder[idx + 1]
            if l in memo:
                l = None
            if r in memo:
                r = None
            memo.append(val)
            if l:
                root.left = TreeNode(val=l, left=None, right=None)
                root = root.left
                parent = root
            elif r:
                root.right = TreeNode(val=r, left=None, right=None)
                root = root.right
                parent = root
            else:
                if parent == None:
                    continue
                root = parent
        return res


# Recursive solution. SC == O(N^2) SC == O(N) Reminds me of quick sort in terms of pivoting
class SolutionV2:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if preorder:
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(val=inorder[idx])
            root.left = self.buildTree(preorder, inorder[0:idx])
            root.right = self.buildTree(preorder, inorder[idx + 1 :])
