from collections import Counter, defaultdict

def minWindowUtil(s: str, t: str) -> str:
    """
    constraint:
    all chars of T should be part of substring you pick from S
    You need to pick minimum such substring

    approach brute force
    --------------------
    substrings = all substrings of S
    min_length = infinity
    for each s in substrings:
          check if all chars of T are in s
          if yes,
              update min_length

    -------------------------
    window approach

    sum of char count in window  == sum of char count in T

    For all chars check, we need to use a Hash of char count of T
    Let w = hash of char count which is empty initially

    S = 'ADOBECODEBANC'
    T = 'ABC'

    W                  T
    -----          -------
    A -> 0          A -> 1
    B -> 0          B -> 1
    C -> 0          C -> 1

    """
    if len(t) > len(s):
        return ""
    target_counter = Counter(t)
    window = defaultdict(int)
    have = 0
    need = len(t)
    left = 0
    right = 0
    min_length = len(s)
    s_len = len(s)
    min_str = ""
    while left <= right < s_len:
        ch = s[right]
        if ch in target_counter:  # if ch is relevant
            window[ch] += 1
            if window[ch] <= target_counter[ch]:
                have += 1
            if have == need:
                while left <= right < s_len and have == need and ((window[s[left]] > 0 and window[s[left]] >= target_counter[s[left]]) or s[left] not in target_counter):
                    if s[left] in target_counter and window[s[left]] >= target_counter[s[left]]:
                        window[s[left]] -= 1
                    if window[s[left]] < target_counter[s[left]]:
                        have -= 1
                    left += 1
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_str = s[left-1:right + 1]

        right += 1
    return min_str


s = 'abdc'
t = 'bc'
#
# s = 'a'
# t = 'aa'
#
# s = 'abcdef'
# t = 'af'

s = 'ADOBECODEBANC'
t = 'ABC'

# s = 'nikhil'
# t = 'ii'
# t = 'n'

s = 'abbbbbbccccddddd'
t = 'bbbcdd'

print(minWindowUtil(s, t))

