# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dummy = TreeNode()
        curr = dummy
        i = 0
        j = 0
        n = len(preorder)

        while i < n and j < n:
            curr.right = TreeNode(preorder[i], right = curr.right)
            curr = curr.right
            i += 1

            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i+=1
            j+=1
            while curr.right and j < n and curr.right.val == inorder[j]:
                prev = curr.right
                curr.right = None
                curr = prev
                j+=1
        return dummy.right