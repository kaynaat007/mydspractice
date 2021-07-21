"""

At any level
    from left to right the length of selection list decreases by 1
"""


def print_combination(nums, k, i, n, perms, output):

    if k == 0:
        output.append(perms.copy())
        return

    for j in range(i, n):
        e = nums[j]
        perms.append(e)
        print_combination(nums, k-1, j+1, n,  perms, output)
        perms.remove(e)


def main(nums, k):
    perms = []
    output = []
    n = len(nums)
    print_combination(nums, k, 0, n, perms, output)
    return output


v = [1, 2, 3]
k = 1
print(main(v, k))



