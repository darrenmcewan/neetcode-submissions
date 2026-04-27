class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def get_ss(n):
            digits = []
            while n > 0:
                digits.append(n%10)
                n//=10
            return sum([x**2 for x in digits])
        
        result = get_ss(n)
        while result != 1:
            if result in seen:
                return False
            seen.add(result)
            result = get_ss(result)
        return True

        