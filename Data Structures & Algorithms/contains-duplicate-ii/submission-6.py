class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            # If the distance between R and L exceeds k,
            # remove the element at index L from the set
            if R - L > k:
                window.remove(nums[L])
                L += 1
            
            # If the current number is already in the set, 
            # it means we found a duplicate within the k-range
            if nums[R] in window:
                return True
            
            # Add the current number to the set
            window.add(nums[R])
        
        return False