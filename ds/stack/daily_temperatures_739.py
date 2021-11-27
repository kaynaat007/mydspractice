from typing import List


def dailyTemperatures(T: List[int]) -> List[int]:

    stack = []
    ans = []
    for e in reversed(T):
        if not stack:
            ans.append(0)
            stack.append((e, 0))
        else:
            if e < stack[-1][0]:
                ans.append(1)
                stack.append((e, 1))
            else:
                c = 0
                while stack and e >= stack[-1][0]:
                    c = c + stack.pop()[1]
                if not stack:
                    stack.append((e, 0))
                    ans.append(0)
                else:
                    stack.append((e, c+1))
                    ans.append(c+1)
    return list(reversed(ans))


T = [10, 2, 6, 1, 7, 12, 5]
T = [10, 12, 20, 25]
T = [25, 20, 12, 10]
T = []
T = [73, 74, 75, 71, 69, 72, 76, 73]
T = [89,62,70,58,47,47,46,76,100,70]  #  [8,1,5,4,3,2,1,1,0,0]
print(dailyTemperatures(T))

