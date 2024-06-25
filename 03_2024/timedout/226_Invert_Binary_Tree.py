# We have to work on the same category for a while.
# I can't get any hang of dfs bfs binary tree concepts. THIS IS PROBLEM.


# TC == O(N) SC == O(logN) ~ O(N). But fragile, not scalable enough. DFS.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        l = root.left
        r = root.right
        root.left = self.invertTree(r)
        root.right = self.invertTree(l)
        return root


from collections import deque


# More robust. BFS.
class SolutionV2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque()
        dq.append(root)
        if root == None:
            return None

        while len(dq):
            node = dq.popleft()
            l = node.left
            node.left = node.right
            node.right = l
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

        return root
