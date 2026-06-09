# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        max_sum = -float('inf')
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        l,r = 0, len(arr) - 1

        while l < r:
            max_sum = max(max_sum, arr[l] + arr[r])
            l+=1
            r-=1
        return max_sum
        