# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #BFS

        q = deque()

        q.append((root,-float('inf'), float('inf')))
        while q:
            node, min_allowed, max_allowed = q.popleft()
            if node.left:
                if node.left.val < node.val and node.left.val > min_allowed:
                    q.append((node.left, min_allowed, node.val))
                else:
                    return False
                
            if node.right:
                if node.right.val > node.val and node.right.val < max_allowed:
                    q.append((node.right, node.val, max_allowed))
                else:
                    return False
        return True
        
