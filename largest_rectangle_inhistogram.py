# Given an array of integers heights representing the
# histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
# 84. Largest Rectangle in Histogram
# ----------------------------------
# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
#
# Example 2:
# Input: heights = [2,4]
# Output: 4
from typing import List

class Solution:
    def largestRectangleArea2(self, heights: List[int]) -> int:
        num_bars = len(heights)
        stack = []
        smaller_left_index = [-1] * num_bars
        smaller_right_index = [num_bars] * num_bars
        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                smaller_right_index[stack[-1]] = index
                stack.pop()
            if stack:
                smaller_left_index[index] = stack[-1]
            stack.append(index)
        max_area = 0
        for i, h in enumerate(heights):
            max_area = max(max_area, h * (smaller_right_index[i] - smaller_left_index[i] - 1))
        return max_area

    def largestRectangleArea1(self, heights: List[int]) -> int:
        # Get the total number of bars in the histogram
        num_bars = len(heights)

        # Initialize stacks for indexes of bars
        stack = []

        # Initialize arrays to record the first smaller bar on the left of each bar
        smaller_left_index = [-1] * num_bars

        # Initialize arrays to record the first smaller bar on the right of each bar
        smaller_right_index = [num_bars] * num_bars

        # Iterate over all heights to compute the smaller_left_index and smaller_right_index
        for index, height in enumerate(heights):
            # Pop elements from the stack while the current height is less than
            # the top element's height in the stack to find the right boundary
            while stack and heights[stack[-1]] >= height:
                smaller_right_index[stack[-1]] = index
                stack.pop()
            # If the stack is not empty, the current element at the top is the previous
            # bar of smaller height (left boundary)
            if stack:
                smaller_left_index[index] = stack[-1]
            # Push this bar onto stack
            stack.append(index)

        # Calculate the maximum area of rectangle in histogram
        max_area = 0
        for i, h in enumerate(heights):
            # Update max_area with the larger area found
            max_area = max(max_area, h * (smaller_right_index[i] - smaller_left_index[i] - 1))

        return max_area

    # optimised code
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len([0] + heights + [0])
        maxArea = 0
        heights.append(0)
        prev_h = 0
        for i, h in enumerate(heights):
            if h == prev_h:
                continue
            prev_h = h
            index = i
            while stack and stack[-1][0] > h:
                old_height, index = stack.pop()
                area = (i - index) * old_height
                if area > maxArea:
                    maxArea = area
            stack.append((h, index))
        return maxArea


s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(s.largestRectangleArea([2, 4]))
