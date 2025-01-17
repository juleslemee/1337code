class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split(" ")
        list1 = [item.strip() for item in list1 if item.strip()]
        print(list1)
        start = 0
        end = len(list1)-1
        while start <= end:
            list1[start], list1[end] = list1[end], list1[start]
            start += 1
            end -= 1
        return ' '.join(list1)