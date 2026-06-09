class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = k
        res = 0
        while r <= len(arr):
            if sum(arr[l:r]) / k >= threshold:
                res +=1
            l+=1
            r+=1

        return res

