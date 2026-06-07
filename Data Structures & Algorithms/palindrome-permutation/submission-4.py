class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        #even must have evemn character counts
        # odd must have all but one even char counts

        s_cnt = Counter(s)

        # Check odd
        if len(s) % 2:
            return sum([s_cnt[x]%2 for x in s_cnt]) == 1
            

        # Check even
        else:
            return not any([s_cnt[x]%2 for x in s_cnt])