class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # State: 
        # dp[i] = cost of reaching step step i

        # step i comes from either step[i-2] or step[i-1]
        # dp[i] = cost[i] + min(step[i-1], step[i-2])
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[n-1], dp[n-2])
        