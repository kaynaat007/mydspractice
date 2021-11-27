"""
problem:

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.


APPROACH 1 my original approach. beats 5% of other solutions only but worth studying.

Very good question on subset sum problem.
Its good because it does not asks to check for a value which is a sum of elements of certain subset in the given array,
but because it uses the logic of that problem + additional complexity of elements being positive or negative.
On top of that, it does not  asks you to find a sum, but it does asks you to find number of ways by which you
can achieve that sum.
Number of ways is essentially leaves  of a binary tree, whose root node is empty. it has two children which are
positive and negative versions of the last element of the array.  Each element further has two children
where it has  +,- of the second  last element of the array. At the leaf, if sum of all elements from root to leaf,
including leaf equals the target sum, then that is 1 way of achieving that sum. Similarly there are other ways of
achieving that target sum. Need to come up with number of ways possible.

Solution :

Number of ways possible is count of such paths from root to leaves wherever sum equals the target sum.

Recursive solution builds upon isSubSetSum recursive solution. isSubsetSum recursive solution is simply based on
following observation

given a target sum S which we need to determine that if its equal to sum of elements of any subset of array,
then,
starting from the last element of the array, we can either
    include that element and recur for sum = target sum - last element, for remaining i - 1 elements or
    or exclude that element and recur for same target sum with i - 1 elements.

    base case will be :
        if i - 1 < 0: return False ( empty array )
        if target == A[i]:
            return True // found the target

To build a recursive solution for the current problem, observe that we cannot exclude the last element and recur.
we must include the element always and recur with +,- versions of it.

    include last element and take + version and recur for target sum - last element with i - 1 elements.
    include last element and take - version and recur for taregt - ( - last element ) with i - 1 elements.

    base case only happens if we hit first element since that will be leaf of our binary tree in the recursion
    process.
    so if i == 0:
        two possibilities:
            A[i] == target:
               Here we have a way of achieving target !
            -A[i] == target:
               Here also we have a way of achieving target

    Optimal substructure:   Observe that the subproblem solution must give us an optimal solution for target sum - last element,
    Only then we can conclude the solution of overall problem.

    Once recursive solution is developed we can see that
    1. recursive version depends on two factors == number of remaining elements and remaining target so a 2 D array will be needed.
    2. base cases help us initialize this 2D array. Consider only 1 element present  in the input array and target sum equals to S
    initialize 2D array dp[i]j] with proper values.
    3. check that to calculate i,j in dp[][], we must need (i-1, target - j) and (i -1, target + j). so iteration
    will happen from left to right in dp array.

    dp array dp[][] will be a n * (2 * sum + 1) array where sum = sum of elements of input array. Given target can
    vary from -sum to sum, hence the size. sp dp[i][j] will represent a tuple (boolean, count).
    boolean will indicate that weather target j is possible in array A[0...i] or not. count indicates that
    if possible, what are number of ways to achieve the same.   j can vary from -sum to +sum.

    Number of ways at any point is just the sum of ways by taking the current element A[i] as positive or negative.
    so essentially ways of achieving a target of j - A[i] by having i - 1 elements and j + A[i] again, by having
    i - 1 elements.

APPROACH 2

"""
def print_matrix(k):
    for i in range(len(k)):
        print(k[i])


def dp_target_sum_with_negative(A, target_sum):

    goal = sum(A)
    n = len(A)
    # goal = target_sum

    if target_sum > goal or target_sum < -goal:
        return 0

    dp = [[[False, 0] for _ in range(-goal, goal + 1)] for _ in range(n)]

    for i in range(-goal, goal + 1):
        c = 0
        if A[0] == i:
            c += 1
            dp[0][i + goal] = [True, c]
        if -A[0] == i:
            c += 1
            dp[0][i + goal] = [True, c]

    for i in range(1, n):
        for j in range(-goal, goal + 1):

            if j - A[i] < -goal:
                v1 = False
                w1 = 0
            else:
                v1, w1 = dp[i - 1][j - A[i] + goal]

            if j + A[i] > goal:
                v2 = False
                w2 = 0
            else:
                v2, w2 = dp[i - 1][j + A[i] + goal]

            if v1 and v2:
                dp[i][j + goal] = [True, w1 + w2]
            elif v1:
                dp[i][j + goal] = [True, w1]
            elif v2:
                dp[i][j + goal] = [True, w2]
            else:
                dp[i][j + goal] = [False, 0]

    return dp[n-1][target_sum + goal][1]


def is_sum_present(A, target, i, c):

    if i < 0:
        return False

    if i == 0:
        if target == A[i]:
            print('found a solution')
            c += 1
            return True
        if target == -A[i]:
            print('found a solution')
            c += 1
            return True
        return False

    c1 = is_sum_present(A, target - A[i], i-1, c)

    c2 = is_sum_present(A, target + A[i], i-1, c)

    return c1 or c2



def is_sum_present_simple(A, target, i, c):
    """

    """
    if i < 0:
        return False
    if target == A[i]:
        c.extend([A[i]])
        c2 = is_sum_present_simple(A, target, i - 1, c)
        return True
    c1 = is_sum_present_simple(A, target - A[i], i-1, c)
    if c1:
        c.extend([A[i]])
    c2 = is_sum_present_simple(A, target, i-1, c)

    return c1 or c2


def dp_subset_sum(A, target):
    """

    """
    n = len(A)
    if n == 0:
        return 0
    total_sum = sum(A)
    if (target + total_sum) % 2 != 0:
        return 0

    modified_target = int((target + total_sum)/2)
    # print('given target : {}'.format(target))
    # print('modified target: {}'.format(modified_target))

    dp = [[[False, 0] for _ in range(modified_target + 1)] for  _ in range(n)]

    for i in range(modified_target + 1):
        if i == A[0]:
            dp[0][i] = [True, 1]

    for i in range(n):
        dp[i][0] = [True, 1]

    if A[0] == 0:
        dp[0][0] = [True, 2]

    for i in range(1, n):
        for j in range(modified_target + 1):

            if j - A[i] < 0:
                w1 = 0
                v1 = False
            else:
                v1, w1 = dp[i-1][j-A[i]]

            v2, w2 = dp[i-1][j]
            if v1 and v2:
                w = w1 + w2
                v = True
            elif v1:
                w = w1
                v = True
            elif v2:
                w = w2
                v = True
            else:
                w = 0
                v = False
            dp[i][j] = [v, w]
    return dp[n-1][modified_target][1]
    # print_matrix(dp)


def findTargetSumWays(nums, target):
        total_sum = sum(nums)
        if total_sum < target:
            return 0
        if (total_sum + target) % 2 > 0:
            return 0
        return dp_subset_sum_v2(nums, int((total_sum + target)/2))


def dp_subset_sum_v2(nums, target):

    print('target -->', target)
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    n = len(nums)

    for i in range(n):
        e = nums[i]
        for j in range(target, e + 1, -1):
            dp[j] += dp[j - e]

    return dp[target]


# A = [1, 3, 5, 6]
# A = [1, 3, 3]
# A = [1, 1]
# A = [2, 4, 1]
A = [1, 1, 1, 1, 1]
# A = [3, 4, 5, 2]
# target = -6
# A = [0,0,0,0,0,0,0,0,1]
target = 3
# print(dp_target_sum_with_negative(A, target))

print(dp_subset_sum(A, target))
print(findTargetSumWays(A, target))