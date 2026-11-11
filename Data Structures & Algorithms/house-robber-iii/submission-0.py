# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root.left and not root.right:
                return root.val, 0
            
            left, leftAlt = 0, 0
            right, rightAlt = 0, 0

            if root.left:
                left, leftAlt = dfs(root.left)
            
            if root.right:
                right, rightAlt = dfs(root.right)
            
            return root.val + leftAlt + rightAlt, \
                max(left + right, left + rightAlt, leftAlt + right, leftAlt + rightAlt)
    
        p, c = dfs(root)

        return max(p, c)