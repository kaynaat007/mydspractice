
def maxProduct(nums) -> int:

    first_max = 0
    second_max = 0
    for i, e in enumerate(nums):
        if e > first_max:
            second_max = first_max
            first_max = e
        elif e > second_max:
            second_max = e

    p = (first_max - 1) * (second_max - 1)

    return p


nums = [3, 4, 5, 2]
nums = [1, 5, 4, 5]
nums = [3, 7]
# nums = [3, 4, 5]
# nums = [5, 4, 3]
# nums = [4, 3]
nums = [1, 2, 3, 16, 8, 9, 25]
print(maxProduct(nums))


