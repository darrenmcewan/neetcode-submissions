# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next
        max_twin_sum = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # middle point is at slow
        prev = None
        curr = slow.next
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        first_half = head
        second_half = prev

        while second_half:
            max_twin_sum = max(max_twin_sum, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next

        return max_twin_sum
        
