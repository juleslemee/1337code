class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def find_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        if ((str1 + str2) != (str2 + str1)):
            return ''
        
        gcd_length = gcd(len(str1), len(str2))
        candidate = (str1)[:gcd_length]
        return(candidate)
            