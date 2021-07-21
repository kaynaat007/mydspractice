"""

At any level
    from left to right the length of selection list decreases by 1.

"""


def is_valid(inp):
    """
    001 == false
    001 ==
    1
    1 == true
    :param inp:
    :return:
    """
    try:
        v = int(inp)
    except ValueError:
        return False

    if int(inp) < 0:
        return False

    if inp == '0':
        return True
    return int(inp) <= 255 and inp[0] != '0'


def print_valid_ips(s, k, i, n,  ans, output):

    if i == n and k == 4:
        output.append(ans.copy())
        return

    if k > 4:
        return

    for j in range(4):
        first_cut = s[i:i + j+1]
        if is_valid(first_cut):
            ans.append(first_cut)
            print_valid_ips(s, k+1, i + j + 1, n, ans, output)
            ans.remove(first_cut)


def main(s):
    k = 0
    i = 0
    n = len(s)
    ans = []
    output = []
    print_valid_ips(s, k, i, n, ans, output)
    return output


s = '12345'
s = '25525511135'
s = '42356'
print(main(s))



