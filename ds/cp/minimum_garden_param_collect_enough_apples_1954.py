'''
number of apples at perimeter of each square of side length l is 12 * l * l. This can be derived by paper and pencil.
number of apples up to square of length l = 12 * 1 * 1 + 12 * 2 * 2 + 12 * 3 * 3 + 12 * 4 * 4 + .......
Follows mono pattern
Binary search can be used.
'''
def minimumPerimeter(neededApples: int) -> int:

    side_length = 0
    total_apples = 0
    while total_apples < neededApples:
        total_apples += (12 * side_length * side_length)
        side_length += 1
    return 8 * (side_length-1)



def minimumPerimeterBinarySearch(neededApples: int) -> int:

    # print('applying binary search')
    low = 1
    high = pow(10, 5)
    ans = 0
    while low <= high:
        side_length = low + (high - low) // 2
        total_apples = (2 * side_length) * (side_length + 1) * (2 * side_length + 1)
        if total_apples >= neededApples:
            high = side_length - 1
            ans = 8 * side_length
        else:
            low = side_length + 1

    return ans





apples = 1000000000
# apples = pow(10, 15)
# apples = 13
# apples = 100
# apples = 45
# apples = 1
# apples = 85
# apples = 2784381467700
apples = 49437
print(minimumPerimeter(apples))
print(minimumPerimeterBinarySearch(apples))

