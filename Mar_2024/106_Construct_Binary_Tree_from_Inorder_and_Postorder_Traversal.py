# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        if postorder:
            try:
                idx = inorder.index(postorder[-1])
                postorder.pop()
            except:
                return
            root = TreeNode(inorder[idx])
            root.right = self.buildTree(inorder[idx + 1 :], postorder)
            root.left = self.buildTree(inorder[0 : idx + 1], postorder)
            return root
