# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(inorder) == 0 or len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)

        inorder_left = inorder[:mid]
        inorder_right = inorder[mid+1:]

        preorder_left = preorder[1:mid+1]
        preorder_right = preorder[mid+1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root
            