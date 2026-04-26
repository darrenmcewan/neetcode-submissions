class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0] * (n+1) #n number of steps + ground
        stairs[0], stairs[1] = 1,1 #ground level + first step are base cases
        for i in range(2,n+1):
            stairs[i] = stairs[i-1] + stairs[i-2]
        return stairs[n]



