

def partition_labels(s):
    """

    (i, i) is default interval of each char
    do something on char seen before
    do something on char not seen before.

    initial solution:
`````
        based on storing interval for each character encountered and stack to keep track of disjoint
        intervals.

        stack always keep track of disjoint intervals.

        if we have seen a char, and stack is not empty
             we pop all intervals from stack which are subset of this given interval
             where givern interval left value is oldest left index of a char
             and right value is current index.

             Now if  given interval can overlap with stack top position
             in this case, we update the stack top position to account for new right index

             else we just push current interval.
        else:
            push each char as (i, i).
            (i, i) is default interval of each char.

    """
    char_to_index = {}
    stack = []
    ans = []
    for i, ch in enumerate(s):

        if ch not in char_to_index:
            char_to_index[ch] = i

        if stack and ch in char_to_index:
            last_index = char_to_index[ch]
            current_index = i

            while stack and stack[-1][0] >= last_index and stack[-1][1] <= current_index:
                stack.pop()

            if stack and stack[-1][0] <= last_index <= stack[-1][1]:
                e = stack.pop()
                stack.append((e[0], current_index))
            else:
                stack.append((last_index, current_index))

        else:
            stack.append((i, i))

    for x, y in stack:
        ans.append((y-x + 1))

    return ans


def partition_v2(s):
    """

    window based approach:  left and right pointer

        approach is to observe that the length of window increases by farthest a char in the window can reach
        to the right
        so keep expanding the window as far right as possible
        when you cannot extend it,
        you will reach the current index == maximum right index
        store the window length
        update window left pointer to next index after current char

    algorithm: ---

    keep the right most index of each char
    while traversing from left to right
        keep track of maximum right index
        if current index == maximum right index
            record this length
            and set left  =  current_index + 1
    """

    char_to_rightmost_index = {ch: i for i, ch in enumerate(s)}
    left = 0
    right = 0
    ans = []
    for i, ch in enumerate(s):

        right = max(right, char_to_rightmost_index[ch])
        if i == right:
            ans.append(right - left + 1)
            left = i + 1
    return ans



s = 'abcabc'
s = 'abc'
# s = 'abcdefabxyzyxz'
# s = 'ababcbacadefegdehijhklij'
# s = 'aaaaaaaaaa'
# s = ''

print(partition_labels(s))
print(partition_v2(s))