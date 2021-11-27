

def findMaximumXOR(nums):

    n = len(nums)
    xor = 0
    for i in range(n):
        for j in range(i+1, n):
            xor = max(nums[i] ^ nums[j], xor)
    return xor

nums = [3, 10, 5, 25, 2, 8]
nums = []
print(findMaximumXOR(nums))