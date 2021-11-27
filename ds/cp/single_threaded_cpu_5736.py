from typing import List
import heapq
from collections import defaultdict
import math


def getOrder(tasks: List[List[int]]) -> List[int]:

    n = len(tasks)
    if n == 0:
        return []
    if n == 1:
        return [0]

    pq = []

    available = defaultdict(list)
    for i, task in enumerate(tasks):
        available[task[0]].append([task[1], i])

    times = list(sorted(available.keys()))
    k = len(times)

    for t in available[times[0]]:
        heapq.heappush(pq, t)

    task_with_shortest_processing_time = heapq.heappop(pq)
    initial_time = times[0]
    output = []
    i = 1
    seen = set()
    remaining_time = initial_time + task_with_shortest_processing_time[0]
    j = 0
    # print(' --- times --- {}'.format(times))
    while j < n:

        while i < k and times[i] <= remaining_time: # while this time, nothing can happen,
            # only new jobs can become available
            if times[i] not in seen:  # we do not want to add same jobs again and again
                for job in available[times[i]]:
                    heapq.heappush(pq, job)
                seen.add(times[i])
            i += 1

        if not pq and i < k:  # if no jobs picked while shortest job was processed and pq is empty,
            # time to go to next times and pick up a job
            for job in available[times[i]]:
                heapq.heappush(pq, job)
            seen.add(times[i])

        # job we started with must finish at this moment and we pick new job
        output.append(task_with_shortest_processing_time[1])

        # after we finish, this is new shortest job possible
        if pq:
            task_with_shortest_processing_time = heapq.heappop(pq)
            # our next time to terminate increased by a factor of task_with_shortest_processing_time's processing time.
            remaining_time = remaining_time + task_with_shortest_processing_time[0]
        j += 1

    return output


tasks = [[1,2],[2,4],[3,2],[4,1]]
# tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
# tasks = [[5, 8], [5, 6]]
# tasks = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]
# [6,1,2,9,4,10,0,11,5,13,3,8,12,7]

# tasks = [[100,100],[1000000000,1000000000]]

print(getOrder(tasks))


