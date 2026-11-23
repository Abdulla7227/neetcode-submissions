class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        stack = []
        max_area = 0

        for i in range(len(heights) + 1):
            curr_height = heights[i] if i < len(heights) else 0

            while stack and curr_height < heights[stack[-1]]:
                h = heights[stack.pop()]
                previous_smaller = stack[-1] if stack else -1

                width = i - previous_smaller - 1
                area = h * width

                max_area = max(max_area, area)

            if i < len(heights):
                stack.append(i)

        return max_area