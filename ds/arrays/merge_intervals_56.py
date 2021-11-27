from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:

    intervals = sorted(intervals, key=lambda key: key[0])

    result = []
    if not intervals:
        return []

    current = intervals[0]
    for interval in intervals[1:]:
        if current[1] >= interval[0]:
            current[1] = max(interval[1], current[1])
        else:
            result.append(current)
            current = interval
    result.append(current)
    return result

intervals = [[1,3],[2,6],[8,10],[15,18]]

# intervals = [[1,4],[4,5]]

intervals = [[1, 3], [10, 20]]

intervals = []

intervals = [[1,4],[2,3]]
print(merge(intervals))

