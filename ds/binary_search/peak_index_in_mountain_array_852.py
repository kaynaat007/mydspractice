from typing import List


def util(arr, low, high, n):

    if low > high:
        return -1

    mid = low + (high - low) // 2
    if  0 <= mid-1 < n and  0 <= mid + 1 < n:

        if arr[mid-1] < arr[mid] < arr[mid+1]:
            return util(arr, mid, high, n)
        elif arr[mid-1] > arr[mid] > arr[mid+1]:
            return util(arr, low, mid, n)
        else:
            return mid
    return -1



def peakIndexInMountainArray(arr: List[int]) -> int:
    n = len(arr)
    return util(arr, 0, n-1, n)

arr =  [0,1,0]
arr = [0,2,1,0]
arr = [0,10,5,2]
arr = [3,4,5,1]
arr = [24,69,100,99,79,78,67,36,26,19]
arr = [3,5,3,2,0]

print(peakIndexInMountainArray(arr))

