class Solution:
    def canPermutePalindrome(self, s: str) -> bool:


        s_cnt = Counter(s)

        odd_counts = sum(count % 2 for count in s_cnt.values())

        return odd_counts <= 1