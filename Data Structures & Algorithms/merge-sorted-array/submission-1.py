class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1ptr = m-1
        nums2ptr = n-1
        if n == 0:
            return

        for i in range(len(nums1)-1,-1,-1):
            if nums2[nums2ptr] >= nums1[nums1ptr]:
                nums1[i] = nums2[nums2ptr]
                nums2ptr -= 1
                if nums2ptr < 0:
                    return
            else:
                nums1[i] = nums1[nums1ptr] 
                nums1ptr -= 1
                if nums1ptr < 0:
                    nums1[:nums2ptr+1] = nums2[:nums2ptr+1]
                    return


        