class Solution:
    def confusingNumber(self, n: int) -> bool:
        inverse_mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        inverse_num = ''
        n = str(n)
        for i in range(len(n)):
            if n[i] not in inverse_mapping:
                return False
            else:
                inverse_num += inverse_mapping[n[i]]
        
        
        return inverse_num[::-1] != n