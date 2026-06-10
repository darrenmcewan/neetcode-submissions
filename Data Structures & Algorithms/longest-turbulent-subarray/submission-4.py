class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # When k is odd k > k+1
        # When k is even k < k+1 
        # or
        # k > k+1 when even
        # k < k+1 when odd
        if len(arr) < 1:
            return 0

        turbulent = 1
        res = 1
        prev_sign = ""
        r = 1
        while r < len(arr):
            if arr[r-1] > arr[r] and prev_sign != ">":
                turbulent += 1
                prev_sign = ">"
                r += 1
            elif arr[r-1] < arr[r] and prev_sign != "<":
                turbulent += 1
                prev_sign = "<"
                r += 1
            else:
                res = max(turbulent, res)
                if arr[r] == arr[r-1]:
                    turbulent = 1
                    prev_sign = ""
                else:
                    turbulent = 2
                    prev_sign = ">" if arr[r-1] > arr[r] else "<"
                r += 1
        return max(res, turbulent)