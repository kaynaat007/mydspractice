'''

6 stages of DP problem:

stage 1: check if dp applies:  optimal substructure + repeated calculations.
stage 2: recursive formula to problem
stage 3: recursive solution
stage 4: top down with memoisation
stage 5: bottom up solution
stage 6: one dimensional solution from bottom up to save space.

'''

from typing import List


def util(nums, i, j, n, turn):
    """

    :param nums:
    :param i:
    :param j:
    :param n:
    :param turn:
    :return:

    This is based on raw observation
    uses turn variable
    calculates max score of alex, max score of bob.
    each player tries to maximise his score
    """

    if j - i + 1 == 1 and 0 <=i < n and 0 <= j < n:
        if turn == 1:
            return nums[i], 0
        return 0, nums[i]

    if i > j:
        return 0, 0

    if turn == 1:
        alex_score_1, bob_score_1 = util(nums, i+1, j, n,  2)
        alex_score_2, bob_score_2 = util(nums, i, j-1, n, 2)
        score1 = nums[i] + alex_score_1
        score2 = nums[j] + alex_score_2
        if score1 > score2:
            return score1, bob_score_1
        return score2, bob_score_2

    if turn == 2:
        alex_score_1, bob_score_1 = util(nums, i+1, j, n, 1)
        alex_score_2, bob_score_2 = util(nums, i, j-1, n, 1)
        score1 = nums[i] + bob_score_1
        score2 = nums[j] + bob_score_2
        if score1 > score2:
            return alex_score_1, score1
        return alex_score_2, score2


def util_no_turn_variable(nums, i, j, n):

    """

    :param nums:
    :param i:
    :param j:
    :param n:
    :return:

    So from the perspective of one player 1, anything he chooses is a plus, and nything his opponent chooses,
    is a minus.
    in each  call what we are calculating is difference between player's scores.
    Whoever chance it is, we don't care, all we care is how optimal score he can get and how large it is than
    his opponent.
    so we only care about alex score - bob score.
    Alex can chose a nums[i], bob is left with array (i+1, j)
    Alex can chose a nums[j], bob is left with array (i, j-1)
    Whatever delta score we get from bob's call to (i+1, j) or (i, j-1),
    we subtract from alex's choice of nums[i] or nums[j] respectively and take max.

    ----
    So assuming the sum of the array it SUM, so eventually player1 and player2 will split the SUM between themselves.
    For player1 to win, he/she has to get more than what player2 gets. If we think from the prospective of one player,
    then what he/she gains each time is a plus,
    while, what the other player gains each time is a minus.
    Eventually if player1 can have a >0 total, player1 can win.


    """

    if j - i + 1 == 1:
        return nums[i]

    if i > j:
        return 0

    max_difference = max(nums[i] - util_no_turn_variable(nums, i+1, j, n), nums[j] - util_no_turn_variable(nums, i, j-1, n))
    return max_difference


def util_no_turn_variable_bottom_up_dp(nums):
    """
    stage 5: bottom up
    if you see corresponding top down util_no_turn_variable() solution, this is straightforward copy.
    """

    n = len(nums)
    table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                table[i][j] = nums[i]

    for l in range(1, n):
        j = l
        for i in range(n-l):
            print(i, j)
            table[i][j] = max(nums[i] - table[i+1][j], nums[j] - table[i][j-1])
            j += 1
    return table[0][n-1]


def util_no_turn_variable_bottom_up_one_dimensional(nums):
    """
    stage 6: bottom up one dimensional
    if you see corresponding top down util_no_turn_variable_bottom_up_dp() solution, this is
    based on just one observation that to calculate (i,j) you need only (i+1, j) and (i-1, j)
    so store solutions to basic subproblems  in 1 day array.
    update the array itself to more complex subproblems untitl you reach final subproblem.

    """

    n = len(nums)
    table = [nums[i] for i in range(n)]

    for l in range(1, n):
        j = l
        for i in range(n-l):
            table[i] = max(nums[i] - table[i+1], nums[j] - table[i])
            j += 1
    return table[0]



def util_top_down(nums, i, j, n, turn, cache):
    """

    :param nums:
    :param i:
    :param j:
    :param n:
    :param turn:
    :param cache:
    :return:

    This is based on raw observation
    uses turn variable
    calculates max score of alex, max score of bob.
    """

    if j - i + 1 == 1 and 0 <=i < n and 0 <= j < n:
        if turn == 1:
            cache[(turn, i, j)] = (nums[i], 0)
            return nums[i], 0

        cache[(turn, i, j)] = (0, nums[i])
        return 0, nums[i]

    if i > j:
        return 0, 0

    # print(cache)

    if (turn, i, j) in cache:
        print('cache hit...')
        return cache[(turn, i, j)]

    if turn == 1:
        alex_score_1, bob_score_1 = util_top_down(nums, i+1, j, n,  2, cache)
        alex_score_2, bob_score_2 = util_top_down(nums, i, j-1, n, 2, cache)
        score1 = nums[i] + alex_score_1
        score2 = nums[j] + alex_score_2
        if score1 > score2:
            cache[(turn, i, j)] = (score1, bob_score_1)
            return score1, bob_score_1

        cache[(turn, i, j)] = (score2, bob_score_2)
        return score2, bob_score_2

    if turn == 2:
        alex_score_1, bob_score_1 = util_top_down(nums, i+1, j, n, 1, cache)
        alex_score_2, bob_score_2 = util_top_down(nums, i, j-1, n, 1, cache)
        score1 = nums[i] + bob_score_1
        score2 = nums[j] + bob_score_2
        if score1 > score2:
            cache[(turn, i, j)] = (alex_score_1, score1)
            return alex_score_1, score1
        cache[(turn, i, j)] = (alex_score_2, score2)
        return alex_score_2, score2


def PredictTheWinner(nums: List[int]) -> bool:

    n = len(nums)
    # alex_score, bob_score = util(nums, 0, n-1, n, 1)
    alex_score, bob_score = util_top_down(nums, 0, n-1, n, 1, {})

    print(alex_score, bob_score)
    return alex_score >= bob_score


def PredictTheWinnerWithDifference(nums: List[int]) -> bool:

    n = len(nums)
    # alex_score, bob_score = util(nums, 0, n-1, n, 1)
    difference = util_no_turn_variable(nums, 0, n-1, n)
    # print('diff', difference)
    # print(alex_score, bob_score)
    return difference >= 0


def PredictTheWinnerWithDifferenceBottomUpDp(nums: List[int]) -> bool:

    n = len(nums)
    difference = util_no_turn_variable_bottom_up_dp(nums)
    # print('diff', difference)
    # print(alex_score, bob_score)
    return difference >= 0


def PredictTheWinnerWithDifferenceBottomUpDpWithOneDimensional(nums: List[int]) -> bool:

    n = len(nums)
    difference = util_no_turn_variable_bottom_up_one_dimensional(nums)
    print('diff', difference)
    # print(alex_score, bob_score)
    return difference >= 0


nums = [1, 2, 3]
nums = [1, 5, 2]
nums = [1, 5, 233, 7]
nums = [1, 5, 233, 7, 9, 10, 20, 5, 5, 7, 10, 20, 45, 78, 23]
# nums = [8, 3, 9]

print(PredictTheWinner(nums))
# print(PredictTheWinnerWithDifference(nums))
# print(PredictTheWinnerWithDifferenceBottomUpDp(nums))
print(PredictTheWinnerWithDifferenceBottomUpDpWithOneDimensional(nums))





