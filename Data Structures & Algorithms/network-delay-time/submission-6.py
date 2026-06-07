class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create an adj List
        adj = defaultdict(list)
        for ui,vi,ti in times:
            adj[ui].append([vi,ti])

        shortest = {}
        minHeap = [[0,k]]
        while minHeap:
            time1, node1 = heapq.heappop(minHeap)
            if node1 in shortest:
                continue

            shortest[node1] = time1

            for node2, time2 in adj[node1]:
                if node2 not in shortest:
                    heapq.heappush(minHeap, [time1+time2, node2])
        return max(shortest.values()) if len(shortest) == n else -1