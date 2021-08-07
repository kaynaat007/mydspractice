'''
This problem teaches us a subtle approach to solving problems
where decision at current index is made by already taking decisions on it's left and right
counterparts.

Assuming we only care if a lower rating child is before a higher rating child, we allocate candies optimally
    --This is our left array


Assuming we only care if a higher rating child is before a lower rating child, we allocate candies optimally
    --This is our right array

Then we build our optimal array where we combine the max candies they were allocated

'''

from typing import List


def candy(ratings: List[int]) -> int:
    n = len(ratings)
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]
    output = [0 for _ in range(n)]
    left[0] = 1
    for i in range(1, n):
        if ratings[i] <= ratings[i-1]:
            left[i] = 1
        else:
            left[i] = 1 + left[i-1]
    right[n-1] = 1
    for i in range(n-2, -1, -1):
        if ratings[i] <= ratings[i + 1]:
            right[i] = 1
        else:
            right[i] = 1 + right[i+1]

    # print(left, right)

    for i in range(n):
        output[i] = max(left[i], right[i])

    # print(output)
    return sum(output)


rating = [1, 2]
rating = [2, 1]
rating = [1, 0, 2]

rating = [1,2,2]
rating = [1, 4, 5, 2, 9, 6]
print(candy(rating))




