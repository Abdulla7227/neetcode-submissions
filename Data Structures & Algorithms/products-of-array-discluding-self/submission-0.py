class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

#left -> right
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix = prefix * nums[i]

#right -> left
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] = output[i] * postfix
            postfix = postfix * nums[i]

        return output 