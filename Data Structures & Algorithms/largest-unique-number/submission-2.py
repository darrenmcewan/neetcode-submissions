class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max_num = -1

        for num in nums:
            if num == max_num:
                max_num = -1
            elif num > max_num:
                max_num = num
            else: 
                return max_num
        return max_num if max_num else -1