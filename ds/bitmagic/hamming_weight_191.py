
def hammingWeight(n: int) -> int:

    # print('bits of {}'.format(x))
    c = 0
    while n:
        if n & 1:
            c += 1
        n = n >> 1
    return c

def killTheFirstZombieWay(n: int) -> int:

    # print('bits of {}'.format(x))
    c = 0
    while n:
        n = n & (n-1)
        c += 1
    return c

n = 11

# n =  32
print(killTheFirstZombieWay(n))
