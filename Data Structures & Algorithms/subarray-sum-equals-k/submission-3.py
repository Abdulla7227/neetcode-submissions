class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count = 0
        

        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i, len(nums)):
        #         total = total + nums[j]
        #         if total == k:
        #             count = count + 1
        # return count
        # this is brute force method
        



  
        count = 0
        current_sum = 0
        prefix_map = {0:1}

        for n in nums:
            current_sum = current_sum + n
            count = count + prefix_map.get(current_sum - k, 0)
            prefix_map[current_sum] = 1 + prefix_map.get(current_sum, 0)

        return count 
            
