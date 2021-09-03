"""

problem :


In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.


example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.

approaches:

recursive

i developed two recursive versions first before arriving at dp solution.

first recursive version

make a choice at index i and then recur for index i + 1

what choice ?

we can either go with day-1 pass, day-7 pass or day-30 pass.
concept of covering is there. say days[i] = 20 and i chose a 7 day pass, so i send 20 + 7 in recursive
call and if next day at i + 1 is well within 27, we do not need to make a choice since we cover that day. we recur for
next day with same cover value.

we return min of three choices at every step.

second recursive version

make a choice at index i, recur for index i - 1.

choices are familiar to you . now we take them at index i and recur for i-1. Take min of
three choices and return.

We need to find the index till the current choice supports us. Say we chose a 7 day pass
so how far we can travel ?
current day - 7 right ? so we need to find an index where it have
condition such that current -day - 7 does not support us. Once we find that, we recur from that index

same with day-30 pass.

dp solution :

tricky part is to find a non supporting index.
Days are numbered from 1 to 365.
so if array is given say [50, 60, 70, 80, 100]
then we can store a day to index mapping.

for day 50 it will 0
for day 51 it will 0 why ? since if some choice supports us till day 51, then, still the day 50 is out of
reach. We need to pay for day 50. How do we pay ? by making a choice again at day 50.
so all days  from 51 to 59 will be mapped to index 0. all of them do not support day 50.

same for all other days.

Once we have that mapping

we can proceed in bottom up fashion

base case is when we have only one day.  we can easily see that cost is min of all day passes.

we start from second index now  and we
add the previous index cost to the most optimal choice we make at this index.

by taking a 7 day pass we go back 7 days before to see till what day we are supported.
if the previous value isn't not supported then simply we add a cost of a 7 day pass to previous cost.
if it is supported, we calculate how far we are supported. Find an index till we aren't supported and
then add the cost till that day to the 7 day pass cost.

same with a 30 day pass.

dp[n-1] stores our answer.

"""

def recursive_min_bill(current_cover, i, n, A, P):

    if i > n - 1:
        return 0

    if current_cover >= A[i]:
        return recursive_min_bill(current_cover, i+1, n, A, P)

    return min(
        P[0] + recursive_min_bill(0, i+1, n, A, P),
        P[1] + recursive_min_bill(7 + A[i] - 1, i+1, n, A, P),
        P[2] + recursive_min_bill(30 + A[i] - 1, i+1, n, A, P)
    )


def recursive_min_bill_v2(i, A, P, dp):
    """

    """
    base_index = i
    if base_index < 0 :
        return 0

    if dp[base_index] != -1:
        print('returning for i {}'.format(i))
        return dp[i]

    c1 = P[0] + recursive_min_bill_v2(base_index-1, A, P, dp)

    seven_day_pass = A[base_index] - 7

    i = base_index
    while i >= 0 and seven_day_pass < A[i]:
        i = i - 1

    c2 = P[1] + recursive_min_bill_v2(i,  A, P, dp)

    thirty_day_pass = A[base_index] - 30
    i = base_index

    while i >= 0 and thirty_day_pass < A[i]:
        i = i - 1

    c3 = P[2] + recursive_min_bill_v2(i,  A, P, dp)

    cost = min(c1, c2, c3)
    dp[base_index] = cost
    print('calculating for i = {}, min cost = {} among {}, {}, {}'.format(base_index, cost, c1, c2, c3))
    return cost


def bottom_up(A, P):

    days_to_index = {}
    n = len(A)
    low = A[0]
    one_day_pass_cost = P[0]
    seven_day_pass_cost = P[1]
    thirty_day_pass_cost = P[2]

    dp = [0 for i in range(n)]
    for i in range(n):
        days_to_index[A[i]] = i
        val = A[i] + 1
        while i + 1 < n and val < A[i+1]:
            days_to_index[val] = i
            val += 1

    dp[0] = min(one_day_pass_cost, seven_day_pass_cost, thirty_day_pass_cost)

    for i in range(1, n):

        previous_cost = dp[i-1]
        previous_day = A[i-1]

        seven_days_back = A[i] - 7
        thirty_day_back = A[i] - 30

        choice_one_day_current_cost = one_day_pass_cost + previous_cost
        choice_seven_day_current_cost = seven_day_pass_cost
        choice_thirty_day_current_cost = thirty_day_pass_cost

        if seven_days_back > previous_day:
            choice_seven_day_current_cost = seven_day_pass_cost + previous_cost
        else:
            if seven_days_back >= low:
                choice_seven_day_current_cost = dp[days_to_index[seven_days_back]] + seven_day_pass_cost

        if thirty_day_back > previous_day:
            choice_thirty_day_current_cost = thirty_day_pass_cost + previous_cost
        else:
            if thirty_day_back >= low:
                choice_thirty_day_current_cost = dp[days_to_index[thirty_day_back]] + thirty_day_pass_cost

        dp[i] = min(choice_one_day_current_cost, choice_seven_day_current_cost, choice_thirty_day_current_cost)





# A = [1,4,6,7,8,20]
# need to have a concept of visited here.
A = [1, 4, 6, 7, 8, 20]
# A = [1,2,3,4,5,6,7,8,9,10,30, 31]
P = [2, 7, 15]
n = len(A)
dp = [-1 for i in range(n)]
# print(recursive_min_bill_v2(len(A) - 1, A, P, dp))
print(bottom_up(A, P))

