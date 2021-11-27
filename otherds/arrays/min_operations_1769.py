from typing import List

def minOperations(boxes: str) -> List[int]:

    if not boxes:
        return []
    output = []
    n = len(boxes)
    for i in range(n):
        count = 0
        for j in range(n):
            if boxes[j] == '1':
                count += abs(i - j)
        output.append(count)

    return output


boxes = '101'
boxes = '110'
boxes = '001011'
print(minOperations(boxes))

