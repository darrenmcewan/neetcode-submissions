class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        # 1. Count card frequencies
        count = Counter(hand)
        
        # 2. Use a min-heap to always pick the smallest available card
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            # The smallest card in the heap must be the start of a group
            first = min_heap[0]
            
            # 3. Try to form a group starting from 'first'
            for i in range(first, first + groupSize):
                if count[i] == 0:
                    # If a consecutive card is missing, we can't form the group
                    return False
                
                count[i] -= 1
                
                # 4. If this card is exhausted, it must be the current minimum
                if count[i] == 0:
                    if i != min_heap[0]:
                        # If the card that ran out isn't the smallest in our heap,
                        # it means we skipped a smaller card earlier, which is impossible.
                        return False
                    heapq.heappop(min_heap)
                    
        return True
