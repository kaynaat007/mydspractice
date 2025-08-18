from typing import List
from bisect import bisect_left


def maxTwoEventsUtil(events: List[List[int]]) -> int:
    events = sorted(events, key=lambda x: x[0])
    n = len(events)
    cache = {}
    return maxTwoEventsUtil4Cache(events, 0, 1, n, 0, cache)


def is_overlap(i, j, events):
    return events[j][0] <= events[i][1]


def maxTwoEventsUtil4(events, k, j, n, prev):
    if j == n and k < n:
        return max(events[k][2], prev)
    elif k == n:
        return prev
    elif is_overlap(k, j, events):
        v1 = maxTwoEventsUtil4(events, k, j+1, n,  events[j][2])
        v2 = maxTwoEventsUtil4(events, j, j+1, n, events[k][2])
        return max(v1, v2, prev)
    else:
        v1 = maxTwoEventsUtil4(events, j+1, j+2, n, events[k][2] + events[j][2])
        v2 = maxTwoEventsUtil4(events, k, j+1, n, events[j][2])
        v3 = maxTwoEventsUtil4(events, j, j+1, n, events[k][2])
        return max(v1, v2, v3, prev)


"""

search for index of element which has start time > end time of current event  

"""
def recursive_maxTwoEventsUtil(events, idx, k):

    if k == 2:
        return 0

    current_start_time = events[idx][0]
    current_end_time = events[idx][1]

    next_valid_candidate_idx = bisect_left(events, )



def maxTwoEventsUtil4Cache(events, k, j, n, prev, cache):

    if (k, j, prev) in cache:
        return cache[(k, j, prev)]
    if j == n and k < n:
        cache[(k, j, prev)] = max(events[k][2], prev)
        return max(events[k][2], prev)
    elif k == n:
        cache[(k, j, prev)] = prev
        return prev
    elif is_overlap(k, j, events):
        v1 = maxTwoEventsUtil4(events, k, j+1, n,  events[j][2])
        v2 = maxTwoEventsUtil4(events, j, j+1, n, events[k][2])
        cache[(k, j, prev)] = max(v1, v2, prev)
        return max(v1, v2, prev)
    else:
        v1 = maxTwoEventsUtil4(events, j+1, j+2, n, events[k][2] + events[j][2])
        v2 = maxTwoEventsUtil4(events, k, j+1, n, events[j][2])
        v3 = maxTwoEventsUtil4(events, j, j+1, n, events[k][2])
        cache[(k, j, prev)] = max(v1, v2, v3, prev)
        return max(v1, v2, v3, prev)


e = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
e = [[1, 5, 3], [1, 5, 1], [6, 6, 5]]
e = [[1,3,2],[4,5,2],[1,5,5]]
e = [[10,83,53],[63,87,45],[97,100,32],[51,61,16]]
# e = [[1, 3, 2], [4, 6, 7], [5, 7, 3]]
# e = [[1, 3, 2], [2, 4, 3], [4, 5, 2]]
e = [[18,54,58],[55,61,81],[97,98,15],[17,76,88],[40,59,71],[58,60,74],[22,71,11],[84,85,42],[32,95,32],[46,52,55],[47,56,47],[46,65,15],[60,99,54],[54,95,54],[52,57,21],[66,99,79],[81,99,98],[90,95,22],[86,86,10],[92,100,33],[10,92,87],[19,33,58],[13,75,69],[68,69,3],[66,93,9],[55,80,73],[84,89,50],[14,87,64],[31,84,90],[1,95,31],[4,96,23],[23,71,93]]
print(maxTwoEventsUtil(e))
