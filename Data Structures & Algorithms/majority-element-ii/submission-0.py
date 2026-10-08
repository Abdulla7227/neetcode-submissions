class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        result = []

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
            if count[nums[i]] == len(nums) // 3 + 1:
                result.append(nums[i])
        return result