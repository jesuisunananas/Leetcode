# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        while stack:
            vertex = stack.pop()
            vertex.left, vertex.right = vertex.right, vertex.left
            if vertex.left:
                stack.append(vertex.left)
            if vertex.right:
                stack.append(vertex.right)
        return root



