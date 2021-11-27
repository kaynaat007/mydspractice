from typing import List
from collections import deque


def count_alive_neigbhours(board, i, j, n, m):

    c = 0
    if i-1 >= 0 and j-1 >= 0 and board[i-1][j-1] & 1:
        c+=1
    if i-1 >= 0 and board[i-1][j] & 1:
        c+=1
    if i-1 >= 0 and j + 1 < m and board[i-1][j+1] & 1:
        c+=1
    if j-1 >= 0 and board[i][j-1] & 1:
        c+= 1
    if i+1 < n and j-1 >= 0 and board[i+1][j-1] & 1:
        c+=1
    if i+1 < n and board[i+1][j] & 1:
        c +=1
    if i + 1 < n and j + 1 < m and board[i+1][j+1] & 1:
        c += 1
    if j + 1 < m and board[i][j+1] & 1:
        c += 1
    return c


def is_dead_or_alive(current_state, alive_n):

    if current_state == 1 and alive_n < 2:
        return 0
    if current_state == 1 and alive_n == 2 or alive_n == 3:
        return 1
    if current_state == 1 and alive_n > 3:
        return 0
    if current_state == 0 and alive_n == 3:
        return 1
    return current_state


def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    n = len(board)
    m = len(board[0])
    q = deque()
    vector = [-1] * 25

    for i in range(n):
        for j in range(m):
            alive_neighbours = count_alive_neigbhours(board, i, j, n, m)
            new_state = is_dead_or_alive(board[i][j], alive_neighbours)
            vector[j] = new_state
        q.append(vector.copy())

        if i >= 2:
            old_row = i - 2
            t = q.popleft()
            for s in range(m):
                board[old_row][s] = t[s]

    left_indexes = [n-1, n-2]
    while q:
        old_row = left_indexes.pop()
        t = q.popleft()
        for s in range(m):
            board[old_row][s] = t[s]

    return board




def gameOfLifeBits(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):

            alive_neighbours = count_alive_neigbhours(board, i, j, n, m)
            new_state = is_dead_or_alive(board[i][j], alive_neighbours)
            if new_state == 1:
                board[i][j] = board[i][j] | 2

    for i in range(n):
        for j in range(m):
            board[i][j] = board[i][j] >> 1


board = [[1]]
# board = [[1,1], [1, 1]]
# board = [[0, 1], [1, 1]]
# board = [[0, 1], [1, 0]]

board = [[0, 1, 0],[0, 0, 1],[1, 1, 1], [0, 0, 0]]

# print(gameOfLife(board))
print(gameOfLifeBits(board))











