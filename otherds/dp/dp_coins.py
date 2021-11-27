"""
Assume we want to make sum S with coins[1], coins[2], coins[3] .... coins[n]

optimal substructure: For a bigger problem w(S, coins[1..i]) we can break it down into two subproblems.

we can either include a coin or we can chose to ignore it.
If we include it, notice that we have made our choice and now subproblem reduces by coins[i] ( if we chose ith coin ), so now we are left with
sum S - coins[i] and same number of coins from 1..n.

But we if exclude the ith coin, then our sum remains same, but now we will work with 1 less coin. i.e coins[1...i-1] .

we need to take min of two approaches.
Notice that if our sum is 0, then no matter how many coins we have , it takes zero number of coins to achieve 0.
however if we have no coins, then to achieve any sum is impossible. impossible represented by INF.

Both subproblems must be optimal since if there were an alternative
subproblem which produces min number of coins, we would replace our current solution with that and that would produce
even minimum number of ways to make sum S. A contradiction.


recursive way to compute optimal.

let w(X[j], coins[1..i]) represent min number of coins to achieve a sum of X[j] with coins[1..i]. we wish to compute

w(X[amount], coins[1...n])

w(X[j], coins[1..i]) = min ( 1 + w(X[j] - coins[i], coins[1..i]), w(X[j], coins[1..i-1])
w(0, coins[1..i]) = 0 for all coins.
w(x[j], 0 ) = INF for all possible amounts.

compute : bottom up approach.

"""

import math


def print_matrix(k):
    for i in range(len(k)):
        print(k[i])


def coin_change(coins, amount):
    n = len(coins)
    w =  [ [0 for j in range(n+1)] for i in range(amount+1)]
    print_matrix(w)

    for i in range(n + 1):
        w[0][i] = 0
    for j in range(amount + 1):
        w[j][0] = math.inf

    w[0][0] = 0

    print_matrix(w)

    for i in range(1, amount+1):
        for j in range(1, n+1):
            if coins[j-1] > i:
                w[i][j] = w[i][j-1]
            else:
                w[i][j] = min(w[i-coins[j-1]][j] + 1, w[i][j-1])
    return w


# coins = [1, 2, 5]
# amount = 11
coins = [2]
amount = 3
w = coin_change(coins, amount)
ans = w[amount][len(coins)]

print('answer: ')
if ans == math.inf:
    print(-1)
else:
    print(ans)

print_matrix(w)






