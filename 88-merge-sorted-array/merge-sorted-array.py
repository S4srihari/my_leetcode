class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """i,j = 0,0
        while i < m+n and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i,nums2[j])
                nums1.pop()
                j += 1
            i += 1
        if n > j:
            nums1[-(n-j):] = nums2[j:]"""

        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1