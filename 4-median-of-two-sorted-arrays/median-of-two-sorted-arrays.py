class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        """nums = sorted(nums1+nums2)
        return nums[(m+n)//2] if (m+n)%2 == 1 else (nums[(m+n)//2] + nums[(m+n)//2 -1])/2"""
        if n == 0:
            return nums1[m//2] if m%2 == 1 else (nums1[m//2] + nums1[(m//2) - 1])/2
        elif m == 0:
            return nums2[n//2] if n%2 == 1 else (nums2[n//2] + nums2[(n//2) - 1])/2
        else :
            i,j = 0,0
            prev2, prev = 0,0
            for _ in range((m+n)//2+1):
                prev2 = prev
                if i < m and j < n: 
                    if nums1[i] <= nums2[j]:
                        prev = nums1[i]
                        i += 1
                    else:
                        prev = nums2[j]
                        j += 1
                elif i < m:
                    prev = nums1[i]
                    i += 1
                else:
                    prev = nums2[j]
                    j += 1                    
            
            if (m+n)%2 == 1:
                return prev
            else :
                return (prev + prev2)/2
                
                