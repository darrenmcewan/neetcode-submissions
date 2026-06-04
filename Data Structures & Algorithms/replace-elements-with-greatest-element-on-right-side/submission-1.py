class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxr = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)-2,-1,-1):
            nxt = arr[i]
            arr[i] = maxr
            maxr = max(maxr, nxt)
            

        return arr
            