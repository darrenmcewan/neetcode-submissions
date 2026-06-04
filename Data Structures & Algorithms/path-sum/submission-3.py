# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # BFS 
        if not root:
            return False
        q = deque()

        q.append((root,root.val))
        
        while q:
            node, sum = q.popleft()

            # check if leaf node
            if not node.left and not node.right:
                if sum == targetSum:
                    return True
            
            if node.left:
                q.append((node.left, sum+node.left.val))
            
            if node.right:
                q.append((node.right,sum+node.right.val))
            
        return False
            
            