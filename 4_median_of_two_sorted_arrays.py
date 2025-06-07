class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        l, u = 0, n
        while l <= u:
            n1 = (l + u) // 2
            m1 = (n + m + 1) // 2 - n1
            n1_max = nums1[n1 - 1] if n1 > 0 else float('-inf')
            n2_min = nums1[n1] if n1 < n else float('inf')
            m1_max = nums2[m1 - 1] if m1 > 0 else float('-inf')
            m2_min = nums2[m1] if m1 < m else float('inf')
            if n1_max <= m2_min and m1_max <= n2_min:
                if (n + m) % 2 == 0:
                    return (max(n1_max, m1_max) + min(n2_min, m2_min)) / 2
                else:
                    return max(n1_max, m1_max)
            elif n1_max > m2_min:
                u = n1 - 1
            else:
                l = n1 + 1