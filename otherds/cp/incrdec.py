
def increase_decrease(A):
    n = len(A)
    A.sort()
    set1 = [A[0]]
    set2 = []
    ans = "YES"
    for i in range(1, n):
        if A[i] != set1[-1]:
            set1.append(A[i])
        elif not set2 or A[i] != set2[-1]:
            set2.append(A[i])
        elif A[i] == set1[-1] and A[i] == set2[-1]:
            ans = "NO"
            break
    if set2:
        if set1[-1] == set2[0]:
            ans = "NO"
    print(ans)
    if ans == "YES":
        for i in range(len(set1)):
            print(set1[i], end=" ")
        if len(set2) > 0:
            for i in reversed(set2):
                print(i, end=" ")



if __name__ == '__main__':
    T = int(input())
    while T:
        N = int(input())
        array = str(input())
        array = [int(item) for item in array.split(' ')]
        increase_decrease(array)
        print('\n')
        T -= 1


s = {'a', 'b'}