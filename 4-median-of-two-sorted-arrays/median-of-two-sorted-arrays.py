class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        nums = sorted(nums1+nums2)
        return nums[(m+n)//2] if (m+n)%2 == 1 else (nums[(m+n)//2] + nums[(m+n)//2 -1])/2
        """if n == 0:
            return nums1[m//2] if m%2 == 1 else (nums1[m//2] + nums1[(m//2) - 1])/2
        elif m == 0:
            return nums2[n//2] if n%2 == 1 else (nums2[n//2] + nums2[(n//2) - 1])/2
        else :
            i,j = 0,0
            prev2, prev = 0,0
            while i+j <= (m+n)//2:
                if i < m and  nums1[i] <= nums2[j]:
                    cur = nums1[i]
                    prev2 = prev
                    prev = cur
                    i += 1
                elif j < n-1:
                    cur = nums2[j]
                    prev2 = prev
                    prev = cur
                    j += 1
            
            if (m+n)%2 == 1:
                return prev
            else :
                return (prev + prev2)/2"""
                
                