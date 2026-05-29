# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half_head = slow.next
        slow.next = None

        # Reverse second half
        prev_node = None
        curr_node = second_half_head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        first_node = head
        second_node = prev_node

        while second_node:
            first_next = first_node.next
            second_next = second_node.next

            first_node.next = second_node
            second_node.next = first_next

            first_node = first_next
            second_node = second_next

        return