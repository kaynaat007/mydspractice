import heapq


def findKthLargest(nums, k):
    """

    """
    n = len(nums)
    heapq.heapify(nums)

    for i in range(n-k):
        heapq.heappop(nums)

    return heapq.heappop(nums)

nums = [1, 2, 3]
nums = [3,2,1,5,6,4]
k = 2
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(nums, k))
