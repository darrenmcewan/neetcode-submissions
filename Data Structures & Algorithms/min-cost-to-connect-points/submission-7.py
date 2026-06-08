class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        def manhattan_dist(x1,y1,x2,y2):
            return abs(x1-x2) + abs(y1-y2)

        # Optimization: Prim's algorithm can be implemented without building a full adjacency list
        # to save memory and construction time, but the TLE is primarily due to the edge-heavy graph.
        n = len(points)

        visited = set()
        minHeap = [[0, 0]] # cost, idx
        heapq.heapify(minHeap)
        total_cost = 0
        count = 0

        while minHeap and count < n:
            cost, point = heapq.heappop(minHeap)

            if point in visited:
                continue
            
            visited.add(point)
            total_cost += cost
            count += 1
            x1, y1 = points[point]
            for next_point in range(n):
                if next_point not in visited:
                    x2, y2 = points[next_point]
                    dist = manhattan_dist(x1, y1, x2, y2)
                    heapq.heappush(minHeap, [dist, next_point])
        return total_cost
