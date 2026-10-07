class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0

        for x in hashset:
            if x - 1 not in hashset:
                current_length = 1

                while x + 1 in hashset:
                    x = x + 1
                    current_length = current_length + 1

                longest = max(longest, current_length)


        return longest

