# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        curr = dummy

        while list1 or list2:
            v1 = list1.val if list1 else 101
            v2 = list2.val if list2 else 101

            if v1 <= v2:
                curr.next = ListNode(v1)
                list1 = list1.next if list1.next else None
            else:
                curr.next = ListNode(v2)
                list2 = list2.next if list2.next else None
            curr = curr.next
        return dummy.next                