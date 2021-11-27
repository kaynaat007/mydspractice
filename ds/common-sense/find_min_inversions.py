"""
Taken from techie delight
"""
import sys


# Function to find the minimum number of inversions needed
# to make the given expression balanced
def findMinInversions(exp):
    # if the expression has an odd length, it cannot be balanced
    if len(exp) % 2:
        return sys.maxsize

    inversions = 0  # stores total inversions needed
    open = 0  # stores the total number of opening braces

    # traverse the expression
    for i in range(len(exp)):

        # if the current character is an opening brace
        if exp[i] == '{':  # exp[i] = '{'
            open = open + 1

        # if the current character is a closing brace
        else:  # exp[i] == '}' here
            # if an opening brace is found before, close it
            if open:
                open = open - 1  # decrement opening brace count
            else:
                # invert the closing brace, i.e., change `}` to `{`
                inversions = inversions + 1  # increment total inversions needed by 1
                open = 1  # increment opening brace count

    # for `n` opened braces, exactly `n/2` inversions are needed
    return inversions + open // 2

exp = '}{{{'
inv = findMinInversions(exp)
print(inv)
