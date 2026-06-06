class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_hash = {0:-1}

        curSum = 0

        for i,num in enumerate(nums):
            curSum += num
            remainder = curSum % k

            if remainder not in remainder_hash:
                remainder_hash[remainder] = i
            elif i-remainder_hash[remainder]>1:
                return True
            
                
        
        return False