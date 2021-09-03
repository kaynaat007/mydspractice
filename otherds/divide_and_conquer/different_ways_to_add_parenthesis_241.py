"""
Think about a * b - c * d

how many ways can you group these numbers ?
All are binary operators.
Divide it into subproblems and solve each recursively

(a) * ( b - c * d ) --- 1
(a * b ) - ( c * d ) --- 2
(a * b - c ) * (d) -- 3

divide step:

    For each operator, two subproblems arise. left and right.
    base case when you are left with one element. That must be a number since on operators we are dividing into
    subproblems.

concquer step:

     say number of possible values of left expression = [4, 5, 6]
     possible values of right expression is  [8, 10]
     then we merge these results into one 1 result.


optimisation:  dict dp is added so to save results and reuse.

"""

class solution:

    def diffWaysAddParen(self, s, i, j, dp):

        ans = []

        if j - i + 1 == 1:
            return [s[i]]

        k = i
        num = ''
        while k <= j:

            ch = s[k]

            if ch in ['+', '-', '*']:  # divide step

                if s[i:k] in dp:
                    l = dp[s[i:k]]
                else:
                    l = self.diffWaysAddParen(s, i, k - 1, dp)  # compute for left expression
                    if l:
                        dp[s[i:k]] = l

                if s[k+1:j+1] in dp:
                    r = dp[s[k+1:j+1]]
                else:
                    r = self.diffWaysAddParen(s, k + 1, j, dp)  # compute for right expression
                    if r:
                        dp[s[k+1:j+1]] = r

                op = ch

                if l and r and op: # merge step
                    for m in l:
                        for n in r:
                            res = eval(str(m) + op + str(n))
                            ans.append(res)
            else:
                num = num + ch

            k = k + 1

        if ans:
            return ans
        elif num:
            return [int(num)]
        else:
            return []



s = '2-1-1'
# s = '2*3-4*5'
# s = '1111+1'
i = 0
j = len(s)-1
dp = {}
print(solution().diffWaysAddParen(s, i, j, dp))








