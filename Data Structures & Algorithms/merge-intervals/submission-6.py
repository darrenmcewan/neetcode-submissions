class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        res = []
        intervals.sort(key=lambda x: x[0])
        min_start, max_end = intervals[0][0], intervals[0][1]

        for interval in intervals:
            start = interval[0]
            end = interval[1]
            if start == min_start and end == max_end:
                continue

            if min_start <= start <= max_end:
                max_end = max(max_end, end)
            else:
                res.append([min_start, max_end])
                min_start = start
                max_end = end
        res.append([min_start, max_end])

            

        return res
