from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)

        return [
            list(set1 - set2), list(set2 - set1)
        ]


sol = Solution()
print(sol.findDifference([1, 2, 3], [2, 4, 6]))
