'''

Approach 1
---
This problem teaches us a subtle approach to solving problems
where decision at current index is made by already taking decisions on it's left and right
counterparts.

Assuming we only care if a lower rating child is before a higher rating child, we allocate candies optimally
    - we assign a candy = 1 to a child
    - if next candidate is lower than this child, we still assign him 1
        - else we assign 1 + current childs' candy.

Assuming we only care if a higher rating child is before a lower rating child from the right hand side,
we allocate candies optimally
   - we assign a candy = 1 to a child
    - if cur next candidate in right  is lower than this child, we still assign 1 + next child's candy
        - else we assign 1 to current child

Then we build our optimal array where we combine the max candies they were allocated at current position

Approach 2
----

Ratings:

Inf                                      Inf
|                   Peak                  |
|       Peak          |                   |
|         |           | |                 |
|       | |           | | |               |
|     | | | |       | | | | |     | | |   |
|   | | | | | |   | | | | | | |   | | |   |
| _ | | | | | | | | | | | | | | _ | | | | |
-------------------------------------------
* 0 2 3 4 5 3 2 1 2 3 6 5 4 3 2 0 3 3 3 1 *
i=0 1 2 3 4 5 6 7 8 9...             ...19


We can also  think of pit approach

We identify pits and we travel left from pit till we encounter a peak
we travel right from pit, till we encounter a pit
if we see a candy already at peak, and we are carrying a candy which is lesser than that, we knock off that
candy and assign this new one

https://leetcode.com/problems/candy/discuss/327158/Intuitive-O(N)-time-and-O(1)-explained-like-a-5th-grader


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




