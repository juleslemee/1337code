class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the answer array to store left products
        answer = [1] * n

        # Calculate left products
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Now use a single variable to track the right product
        right_product = 1
        for i in range(n - 1, -1, -1):
            # Multiply the current answer[i] by the running right product
            answer[i] *= right_product
            # Update the right product
            right_product *= nums[i]

        return answer
