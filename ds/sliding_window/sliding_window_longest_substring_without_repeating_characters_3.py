"""
classic two pointer

maintain a window of [slow, fast]

keep expanding unless a repeat char found.
Once found, shrink it by index of this char found in past for the current window.
   update current length = fast - slow + 1 since slow has moved forward.

"""

def longest_substring_no_repeat_char(s):

    char_map = {}
    n = len(s)
    slow = 0
    fast = 0
    curr_length = 0
    ans = 0
    i = 0
    while slow < n and fast < n:

        ch = s[fast]
        if ch in char_map and char_map[ch] >= slow: # do something when repeat found. shrink the window.
            # check that weather in a window [slow, fast], any occurence of s[fast] happens since s[fast] is what's new.
            slow = char_map[ch] + 1
            curr_length = fast - slow + 1
            fast = fast + 1
        else:
            fast = fast + 1  # keep exapnding unless a repeat found.
            curr_length += 1

        char_map[ch] = i  # keep latest index of a given char in hash. we need latest because our window shifts and
        # we would not want to refer to an invalid index of same char. for eg if b occurs twice, maintain only
        # latest index of b.
        ans = max(ans, curr_length)
        i = i + 1

    return ans



def longest_substring_no_repeat_fast(s):

    """
    optimsation is to use array instead of hash lookup.

    """

    char_map = [-1] * 256
    n = len(s)
    slow = 0
    fast = 0
    curr_length = 0
    ans = 0
    i = 0
    while slow < n and fast < n:

        ch = s[fast]
        asc = ord(ch)

        if char_map[asc] != -1 and char_map[asc] >= slow: # do something when repeat found. shrink the window.
            # check that weather in a window [slow, fast], any occurence of s[fast] happens since s[fast] is what's new.
            slow = char_map[asc] + 1
            curr_length = fast - slow + 1
            fast = fast + 1
        else:
            fast = fast + 1  # keep exapnding unless a repeat found.
            curr_length += 1

        char_map[asc] = i  # keep latest index of a given char in hash. we need latest because our window shifts and
        # we would not want to refer to an invalid index of same char. for eg if b occurs twice, maintain only
        # latest index of b.
        ans = max(ans, curr_length)
        i = i + 1
    return ans

s = 'abcabcbb' # exp 3
# s = 'bbbbb' # exp 1
# s = 'pwwkew' # exp 3
# s = 'abba' # exp 2
# s = 'abbbbaaaaaaaaadefghijkaaaaaa'
print(longest_substring_no_repeat_char(s))
print(longest_substring_no_repeat_fast(s))