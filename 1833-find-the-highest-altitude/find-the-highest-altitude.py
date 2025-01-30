class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = maxAlt = 0
        change = 0
        while change < len(gain):
            alt += gain[change]
            maxAlt = max(alt, maxAlt)
            change += 1
        return maxAlt