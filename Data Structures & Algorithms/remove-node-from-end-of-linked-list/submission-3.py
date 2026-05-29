# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        remove_node = length - n

        dummy = ListNode()
        curr = dummy
        curr.next = head

        i = 0
        while True:
            if i != remove_node:
                curr = curr.next
                i += 1
            else:
                curr.next = curr.next.next
                break
        return dummy.next
