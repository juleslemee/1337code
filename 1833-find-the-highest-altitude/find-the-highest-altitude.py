class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = maxAlt = 0
        for change in gain:
            alt += change
            maxAlt = max(alt, maxAlt)
        return maxAlt