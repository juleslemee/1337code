class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProducts = [1]*n
        rightProducts = [1]*n
        answer = [1]*n

        for i in range(1, n):
            leftProducts[i] = leftProducts[i-1] * nums[i-1]

        for i in range(n - 2, -1, -1):
            rightProducts[i] = rightProducts[i+1] * nums[i+1]

        for i in range(n):
            answer[i] = leftProducts[i] * rightProducts[i]

        return answer
'''
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]
            product = 1
            for num in temp:
                product *= num
            answer.append(product)
        return answer
'''