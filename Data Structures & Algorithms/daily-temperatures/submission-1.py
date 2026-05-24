class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp_idx = []

        for i, temp in enumerate(temperatures):
            while temp_idx and temp > temp_idx[-1][0]:
                idx = temp_idx.pop()
                res[idx[1]] = i-idx[1]
            
            temp_idx.append((temp,i))
            
        return res