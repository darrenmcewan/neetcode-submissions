class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euc_distance(x,y):
            return math.sqrt((0-x)**2 + (0-y)**2)
        
        points.sort(key=lambda x: euc_distance(x[0],x[1]))
        return points[:k]