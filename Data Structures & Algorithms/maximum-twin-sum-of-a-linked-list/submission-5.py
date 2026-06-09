class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        max_twin_sum = 0
        
        # Use a list to store values for easier twin indexing
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
            
        n = len(values)
        for i in range(n // 2):
            twin_sum = values[i] + values[n - 1 - i]
            if twin_sum > max_twin_sum:
                max_twin_sum = twin_sum

        return max_twin_sum