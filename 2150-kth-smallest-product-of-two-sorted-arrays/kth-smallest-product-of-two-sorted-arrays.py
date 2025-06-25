class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                res.append(nums1[i]*nums2[j])
        return sorted(res)[k-1]"""

        def cnt(x):
            count = 0
            for a in nums1:
                if a > 0:
                    # a * b <= x => b <= x // a
                    count += bisect_right(nums2, x // a)
                elif a < 0:
                    # a * b <= x => b >= ceil(x / a)
                    # careful with negatives
                    target = x // a
                    if x % a != 0:
                        target += 1
                    count += len(nums2) - bisect_left(nums2, target)
                else:
                    if x >= 0:
                        count += len(nums2)  
            return count

        left, right = -1e10, 1e10
        res = None
        while left <= right:
            mid = int(left + (right-left)//2)
            if cnt(mid) >= k:
                res = mid
                right = mid -1
            else :
                left = mid + 1
        return res