class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        l,r = 1, max(piles)
        min_eating_rate = max(piles)

        def find_hour(piles, k):
            return sum([math.ceil(x/k) for x in piles])

        while l <= r:
            middle = (l+r) // 2

            if find_hour(piles, middle) <= h:
                min_eating_rate = middle
                r = middle - 1
            else:
                l = middle + 1
            
        return min_eating_rate