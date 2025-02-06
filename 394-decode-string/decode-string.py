class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curString = ""
        number = 0
        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char == '[':
                stack.append((curString, number))
                curString = ""
                number = 0
            elif char == ']':
                prev_string, repeat_count = stack.pop()
                curString = prev_string + curString * repeat_count
            else:
                curString += char

        return curString