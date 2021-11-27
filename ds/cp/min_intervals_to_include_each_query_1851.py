from typing import List
import math
from collections import defaultdict, OrderedDict
import heapq


def binary_search_util(arr, low, high, target, ans):

    if low > high:
        return

    mid = low + (high - low) // 2
    mid_element = arr[mid][0]

    if mid_element == target:
        ans[0] = mid
        return binary_search_util(arr, low, mid-1, target, ans)
    elif target < mid_element:
        ans[0] = mid
        return binary_search_util(arr, low, mid - 1, target, ans)
    else:
        return binary_search_util(arr, mid+1, high, target, ans)


def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:

    output = []
    store = defaultdict(list)
    possible_sizes = set()
    for a, b in intervals:
        current_size = b - a + 1
        possible_sizes.add(current_size)
        store[current_size].append((a, b))

    for key, values in store.items():
        values = sorted(values, key=lambda x: x[0])
        store[key] = values

    # print(store)
    # print(possible_sizes)

    possible_sizes = sorted(possible_sizes)
    for target in queries:
        final_ans = -1
        for current_size in possible_sizes:
            values = store[current_size]
            low = 0
            high = len(values) - 1
            ans = [False]
            binary_search_util(values, low, high, target, ans)
            if ans[0]:
                final_ans = current_size
                break
        output.append(final_ans)

    return output


def minIntervalOptimisedByHeap(intervals: List[List[int]], queries: List[int]) -> List[int]:
    """
    process each query method
    heap maintains a set of valid intervals
    for each query,
        insert potentially overlapping intervals into heap
        remove from heap if top most item does not overlap
        report the answer

    :param intervals:
    :param queries:
    :return:

    """

    queries = sorted([(q, i)for i, q in enumerate(queries)], key=lambda x: x[0])
    intervals = sorted(intervals, key= lambda x: x[0])
    first = 0
    n = len(intervals)
    m = len(queries)
    heap = []
    output = [-1 for _ in range(m)]
    # print('sorted interval: {}'.format(intervals))

    for i in range(m):

        current_query = queries[i][0]
        current_query_index = queries[i][1]

        while first < n and intervals[first][0] <= current_query:
            a, b = intervals[first]
            current_interval_size = b - a + 1
            heapq.heappush(heap, (current_interval_size, b))
            first += 1

        while heap and current_query > heap[0][1]: # effectively pop the items from heap if current query does not
            # overlaps
            heapq.heappop(heap)

        if heap:
            size, _ = heap[0]
            output[current_query_index] = size

    return output





def minIntervalOptimisedByBinarySearch(intervals: List[List[int]], queries: List[int]) -> List[int]:
    """
    status: TLE but good approach
    will work if we find a data structure which will maintain it's sorted order
    even after deleting from it multiple times.

    for each interval of smallest --> highest
        let a, b be the interval
        find a lowest query in sorted query array such that it's >= a
        then from this point, check all queries which fall in the interval
        report answer.  
    :param intervals:
    :param queries:
    :return:

    """
    store = OrderedDict()
    for i, e in enumerate(queries):
        store[i] = (e, i)
    queries = sorted([(q, i) for i, q in enumerate(queries)], key=lambda x: x[0])

    # print(store)
    intervals = sorted(intervals, key=lambda x: x[1] - x[0] + 1)
    n = len(intervals)
    m = len(queries)
    output = [-1 for _ in range(m)]
    # print('sorted interval: {}'.format(intervals))

    for i in range(n):
        a,b = intervals[i]
        if not queries:
            break
        low = 0
        high = len(queries) - 1
        m = len(queries)
        ans = [-1]
        binary_search_util(queries, low, high, a, ans)
        lowest_index = ans[0]
        while lowest_index != -1 and lowest_index < m and queries[lowest_index][0] <= b:
            j = queries[lowest_index][1]
            output[j] = b - a + 1
            store.pop(j)
            lowest_index += 1

        queries = sorted(list(store.values()), key=lambda x: x[0])
        # queries = list(store.values())

    return output


intervals = [[1,4], [2, 4], [2, 4]]
queries = [4, 5, 6]


intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4,5]
#

intervals = [[2,3],[2,5],[1,8],[20,25]]
queries = [2,19,5,22]

# intervals = [[4,5],[5,8],[1,9],[8,10],[1,6]]
# queries = [7,9,3,9,3] #  [4,3,6,3,6], [9, 9, 6, 9, 6]

# print(minInterval(intervals, queries))

# intervals = [[3, 4]]
# queries = [3, 4, 5, 6]

intervals = [[54,82],[55,66],[81,89],[38,67],[81,86],[47,47],[13,61],[33,39],[61,66],[97,97],[52,68],[96,98],[89,92],[1,41],[81,89],[9,57],[81,90],[41,73],[29,80],[98,98],[61,95],[93,98],[5,65],[91,96],[91,99],[28,68],[55,71],[35,45],[1,89],[48,48],[26,36],[5,83],[20,83],[73,92],[69,69],[77,89],[12,52],[5,53],[33,53],[70,83],[81,98],[69,69],[28,90],[9,77],[40,53],[53,71],[7,55],[7,28],[5,88],[61,68],[25,93],[45,73],[13,51],[27,70],[47,87],[71,91],[93,98],[1,35],[24,39],[86,90],[19,33],[1,69],[21,100],[85,85],[99,99],[25,25],[90,94],[13,61],[69,85],[89,97],[1,43],[11,35],[41,95],[31,99],[86,94],[33,63],[22,91],[61,75],[71,83],[31,85],[28,83],[1,21],[81,97],[5,29],[74,83],[33,83],[13,24],[92,94],[71,71],[59,79],[21,37],[33,87],[97,97],[34,57],[11,59],[57,62],[22,23],[13,53],[84,85],[71,80]]
queries = [31,9,21,91,91,58,13,76,21,69,41,1,73,2,71,51,69,89,31,85,61,61,39,76,36,50,1,33,41,38,29,91,93,47,1,11,33,79,15,7,21,36,65,1,1,93,45,51,33,5,15,65,49,81,59,21,1,7,81,6,1,80,81,21,24,41,47,85,38,26,100,33,57,24,71,16,65,96,81,83,17,75,76,21,85,47,77,49,31,61,9,49,1,73,32,66,96,97,30,21]

# intervals = [[3, 6]]
# queries = [7]

print(minIntervalOptimisedByHeap(intervals, queries))
print(minIntervalOptimisedByBinarySearch(intervals, queries))