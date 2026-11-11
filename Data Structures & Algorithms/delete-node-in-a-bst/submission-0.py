# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            if not root.left.right:
                root.left.right = root.right
                return root.left
            if not root.right.left:
                root.right.left = root.left
                return root.right

            leftRightMostParent = root.left

            while leftRightMostParent.right.right:
                leftRightMostParent = leftRightMostParent.right
            
            newRoot = leftRightMostParent.right
            newRoot.left = root.left
            newRoot.right = root.right
            leftRightMostParent.right = None
            return newRoot
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root        