# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals: List[List[int]]) -> List[List[int]]:
            intervals.sort(key=lambda x: x[0])
            merged_intervals = [intervals[0]]
            for start, end in intervals[1:]:
                if merged_intervals[-1][1] < start:
                    merged_intervals.append([start, end])
                else:
                    merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
            return merged_intervals

        intervals.append(newInterval)
        return merge(intervals)

    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals: List[List[int]]) -> List[List[int]]:
            # First we sort the intervals based on the starting times.
            intervals.sort(key=lambda x: x[0])
            merged_intervals = [intervals[0]]  # Initialize with the first interval.

            # Iterate through the rest of the intervals to merge overlapping ones.
            for start, end in intervals[1:]:
                # If the current interval does not overlap with the last merged interval.
                if merged_intervals[-1][1] < start:
                    merged_intervals.append([start, end])  # Keep it separate.
                else:
                    # They overlap, so we merge them by updating the end time of
                    # the last interval in the merged list if needed.
                    merged_intervals[-1][1] = max(merged_intervals[-1][1], end)

            # Return the merged list of intervals.
            return merged_intervals

        # Add the new interval to the existing list of intervals.
        intervals.append(newInterval)

        # Call the merge function to merge any overlapping intervals including the new one.
        return merge(intervals)

    # other solution
    def insert3(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            newIntervals.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        newIntervals.append(newInterval)
        while i < len(intervals):
            newIntervals.append(intervals[i])
            i += 1
        return newIntervals

s=Solution()
print(s.insert([[1,3],[6,9]], [2,5]))
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))



