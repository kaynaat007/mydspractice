from typing import List


def place(queen_i, queen_j, m, n, s):
    """

    :param queen_i: source queen x
    :param queen_j:
    :param m:
    :param n:
    :param s:
    :return:  if m & n ca be killed by queen, return False. (m,n) are not safe.
    return True if (m,n) is safe.
    """

    if queen_i == m:
        return False
    if queen_j == n:
        return False
    return not abs(queen_i - m) == abs(queen_j-n)

# print(place(0, 0, 2, 0, 4))

def find_place(q, i, j, n):
    """
    if we can place at (i,j) safely, return True
    else False
    """

    if not q:
        return True
    for pos_x, pos_y in q:
        if not place(pos_x, pos_y, i, j, n):
            return False
    return True

# q = [(0,0)]
# print(find_place(q, 1, 2, 3))


def backtrack(q, k, n, result):

    if k == n:
        sol = []
        for x, y in q:
            ans = ""
            for w in range(n):
                if y == w:
                    ans += 'Q'
                else:
                    ans += '.'
            sol.append(ans)
        result.append(sol)
        return

    for i in range(n):
        # print('placing {}, {}'.format(k, i))
        if find_place(q, k, i, n):
            q.append((k, i))
            backtrack(q, k+1, n, result)
            q.pop()


def solveNQueens(n: int) -> List[List[str]]:

    q = []
    result = []
    backtrack(q, 0, n, result)
    return result


n = 4
print(solveNQueens(n))


