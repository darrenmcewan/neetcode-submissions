class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        currComb = []

        def combRecurion(i, currComb, combinations, k):
            if len(currComb) == k:
                combinations.append(currComb.copy())
                return 

            if i > n:
                return 

            
            # include i
            currComb.append(i)
            combRecurion(i+1, currComb, combinations, k)
            currComb.pop()
            # skip i
            combRecurion(i+1, currComb, combinations, k)

        
        combRecurion(1, currComb, combinations, k)

        return combinations


        
        
