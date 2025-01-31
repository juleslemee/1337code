class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        set1 = set(nums1)
        set2 = set(nums2)
        list1 = list(set1-set2)
        list2 = list(set2-set1) 
        answer.append(list1)
        answer.append(list2)
        return answer
        