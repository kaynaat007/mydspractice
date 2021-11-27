import itertools

#
# def runningSum(nums):
#     output = []
#     s = 0
#     for e in nums:
#         s = s + e
#         output.append(s)
#     return output

def runningSum(nums):
    return list(itertools.accumulate(nums))

nums = [1, 2, 3, 4]
nums = [1,1,1,1,1]
nums = [3,1,2,10,1]
print(runningSum(nums))
