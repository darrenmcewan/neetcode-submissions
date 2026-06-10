class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        prefix = []
        for num in nums:
            total += num
            prefix.append(total)
        
        total = 0
        postfix = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            total += nums[i]
            postfix[i] = total


        for i in range(len(prefix)):
            if prefix[i] == postfix[i]:
                return i
        return -1  

        
        