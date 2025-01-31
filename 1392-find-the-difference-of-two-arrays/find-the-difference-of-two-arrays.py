class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        list1 = list(set(nums1)-set(nums2))
        list2 = list(set(nums2)-set(nums1)) 
        answer.append(list1)
        answer.append(list2)
        return answer
        