

def min_coins(s, n):

    if n == s:
        return 1
    if s == 1:
        return 1
    if s <= n:
        if s % 2 == 0:
            return  1
        else:
            return  2
    else:
        coins = int(s/n)
        s = s % n
        if s == 0:
            return coins
        if s == 1:
            return  1 + coins
        if s % 2 == 0:
            return  1 + coins
        else:
            return  2 + coins


if __name__ == '__main__':
    T = int(input())
    while T:
        cases = str(input()).split(' ')
        s = int(cases[0])
        n = int(cases[1])
        print(min_coins(s, n))
        T -= 1

