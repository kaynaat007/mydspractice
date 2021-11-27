

def recursive_max_points(points, k, i, j):
    if i > j:
        return 0

    if k == 0:
        return 0

    left = points[i] + recursive_max_points(points, k-1, i+1, j)
    right = points[j] + recursive_max_points(points, k-1, i, j-1)

    return max(left, right)


def max_points(points, k):

    n = len(points)
    left = 0
    right = n - 1
    left_sum = 0
    right_sum = 0
    while left < right:

        if points[left] > points[right]:
            left_sum += points[left]
            left = left + 1
            k = k - 1
        else:
            right_sum += points[right]
            right -= 1
            k = k - 1

        if k == 0:
            break

    if k != 0:
        return left_sum + right_sum + points[left]
    else:
        return left_sum + right_sum




# points = [1,2,3,4,5,6,1]
# k = 3

#

points =  [2,2,2]
k = 2


#
# points = [9,7,7,9,7,7,9]
# k = 7



#
# points = [1,1000,1]
# k = 1


# points = [1,79,80,1,1,1,200,1]
# k = 3


# points = [100,40,17,9,73,75]
# k = 3

points = [10, 6, 7, 3, 1, 6, 10]
k = 3

points = [11,49,100,20,86,29,72]
k = 4

print(max_points(points, k))
n = len(points)

print(recursive_max_points(points, k, 0, n-1))