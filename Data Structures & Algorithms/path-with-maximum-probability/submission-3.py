class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = defaultdict(list)

        for i in range(len(edges)):
            adj_list[edges[i][0]].append((edges[i][1],succProb[i]))
            adj_list[edges[i][1]].append((edges[i][0],succProb[i]))

        
        highest = {}
        maxHeap = [[1.0,start_node]]
        heapq._heapify_max(maxHeap)

        while maxHeap:
            prob, node = heapq._heappop_max(maxHeap)
            if node in highest:
                continue
            highest[node] = prob

            if node == end_node:
                break

            for node2, prob2 in adj_list[node]:
                if node2 not in highest:
                    heapq.heappush_max(maxHeap,[prob*prob2, node2])
        return highest.get(end_node, 0.0)