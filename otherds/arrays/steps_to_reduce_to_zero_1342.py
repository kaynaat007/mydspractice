
def numberOfSteps (num: int) -> int:

    count = 0
    while num:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num -  1
        count += 1

    return count


"""
if last bit is 0, it is even number. shift by 1 right to divide by 2. update count to 1 
if last bit is 1, it is odd number, subtract a 1 and then divide by 2, updated count to 2 

special case handling of 1: 

if only subtract by 1 to get to 0 

"""
def numberOfStepsWithBits (num: int) -> int:

    count = 0
    while num:
        if num & 1:
            num = num - 1
            num = num >> 1
            count = count + 2
        else:
            num = num >> 1
            count = count + 1

    return count - 1

print(numberOfStepsWithBits(123))
