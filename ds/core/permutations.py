"""
 At any level
     from left to right the length of selection list remains constant
"""


def print_permutation(nums, perms, output):

    if not nums:
        output.append(perms.copy())
        return

    for i, e in enumerate(nums):
        perms.append(e)
        nums.remove(e)
        print_permutation(nums, perms, output)
        perms.remove(e)
        nums.insert(i, e)


def main(nums):
    """

    """
    perms = []
    output = []
    print_permutation(nums, perms, output)
    return output

v = [1, 2, 3, 4]

# v = [1]
# v = [1,2]
print(main(v))




