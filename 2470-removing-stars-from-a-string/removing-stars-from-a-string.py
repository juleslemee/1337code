class Solution:
    def removeStars(self, s: str) -> str:
        end = []

        for char in s:
            if char == "*":
                end.pop()
            else:
                end.append(char)
        
        return "".join(end)