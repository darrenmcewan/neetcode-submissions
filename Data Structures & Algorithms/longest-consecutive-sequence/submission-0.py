class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec_nums = set()
        max_count=0
        for num in nums: 
            if num - 1 not in consec_nums:
                start = num
                while start+1 in nums:
                    start+=1
                max_count = max(max_count, start-num+1)
            consec_nums.add(num)
        return max_count

