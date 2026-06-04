class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def rec(l,r):
            if l > r:
                return -1
            
            m = (l+r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                return rec(m+1,r)
            else:
                return rec(l,m-1)
            
        return rec(0,len(nums)-1)