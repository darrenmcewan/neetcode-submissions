# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None
        
        
        # Reverse 2nd half 
        prev, curr = None, second_half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        

        first_half = head

        while prev:
            tmp1 = first_half.next
            tmp2 = prev.next
            first_half.next = prev
            prev.next = tmp1 
            first_half = tmp1
            prev = tmp2
        
        return 

        
        
            

        