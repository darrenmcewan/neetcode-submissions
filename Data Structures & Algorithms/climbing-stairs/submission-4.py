class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        
        prev2, prev1 = 1,1 #base cases
        for i in range(2,n+1):
            prev2,prev1 = prev1,prev2+prev1
        return prev1