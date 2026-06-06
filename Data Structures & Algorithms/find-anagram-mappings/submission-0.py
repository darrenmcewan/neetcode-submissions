class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping2 = defaultdict(list)
        for i, num in enumerate(nums2):
            mapping2[num].append(i)
        
        output = []

        for num in nums1:
            output.append(mapping2[num].pop())

        
        return output