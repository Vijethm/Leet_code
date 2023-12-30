class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        ans = []
        for start, end in intervals:
            if not ans or start > ans[-1][1]:
                ans.append([start, end])
            elif start <= ans[-1][1] and end > ans[-1][1]:
                ans[-1][1] = end
        
        return ans