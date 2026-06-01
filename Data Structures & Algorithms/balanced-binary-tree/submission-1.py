# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return 0
            return max(height(root.left), height(root.right)) + 1
        
        if not root:
            return True
        
        # Check height of current node
        left_h = height(root.left)
        right_h = height(root.right)
        
        # The root must be balanced AND children must be balanced
        return (abs(left_h - right_h) <= 1 and 
                self.isBalanced(root.left) and 
                self.isBalanced(root.right))