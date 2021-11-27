
def util(n, turn):

    if n <= 3:
        if turn == 1:
            return True, False
        return False, True

    if turn == 1:

        alex1, bob1 = util(n-1, 2) # alex wins,
        alex2, bob2 = util(n-2, 2)
        alex3, bob3 = util(n-3, 2)

        if alex1:
            return alex1, bob1
        if alex2:
            return alex2, bob2
        if alex3:
            return alex3, bob3

        return False, bob1 and bob2 and bob3

    if turn == 2:

        alex1, bob1 = util(n - 1, 1)
        alex2, bob2 = util(n - 2, 1)
        alex3, bob3 = util(n - 3, 1)

        if bob1:
            return alex1, bob1
        if bob2:
            return alex2, bob2
        if bob3:
            return alex3, bob3

        return alex1 and alex2 and alex3, False

def canWinNimV2(n: int) -> bool:

    if n > 3 and n % 4 == 0:
        return False
    return True


def canWinNim(n: int) -> bool:

    alex, bob = util(n, 1)
    print(alex, bob)
    return alex


n = 19
print(canWinNim(n))
print(canWinNimV2(n))



