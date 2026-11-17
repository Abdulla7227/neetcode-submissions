class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
               prev_index = stack.pop()
               result[prev_index] = i - prev_index

            stack.append(i)

        return result 





#         monotionic stack problem learn the code
#         stack = []	Create an empty stack
# for i ...	                          Visit each element
# while stack	                          Make sure stack isn't empty
# nums[i] > nums[stack[-1]]	          Check whether current element is greater than the top
# stack.pop()	                          Remove elements that have found their next greater element
# stack.append(i)	                      Store the current index for future comparisons

        