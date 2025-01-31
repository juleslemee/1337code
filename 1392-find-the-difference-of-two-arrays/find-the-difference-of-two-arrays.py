class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1 = list(set(nums1)-set(nums2))
        list2 = list(set(nums2)-set(nums1)) 
        answer = [list1, list2]
        return answer
        