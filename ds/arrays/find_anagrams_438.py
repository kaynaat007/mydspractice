"""
Took time to come up with this Sliding window.

Two cases for current character ch of s:

ch can be in anagram list of chars

    Here it's bit tricky
    We need to check if count[ch] is positive
    if it is, we decrement the count and decrement our total counter k
    if it is not, which means it's zero . This is trickiest
        Think when will count of ch will become zero. When the requirement of ch finishes.
        so ch came and we saw count[ch] is already zero, this means there is no rrquirement of ch at the moment.
        See that chars between [start, end-1] at this moment are still part of anagram chars.
        so here we shift the start pointer till we meet an instance of ch.
        We increment all counts of characters in this process because we need fresh in the new window.
        we update our k to be n - (end - start) which is number of chars remaining to be found to satisfy anagram reqs.

ch is not in anagram list of chars
    Here we know how to slide window.
    Move past the ch's position

k == 0

so we found an anagram

"""
from typing import List
from collections import Counter


def findAnagrams(s: str, p: str) -> List[int]:

    count = Counter(p)
    output = []
    start = 0
    end = start
    n = len(p)
    k = n
    s_len = len(s)
    p_len = len(p)

    if p_len > s_len:
        return output

    while 0 <= start <= end < s_len:

        ch = s[end]

        if ch not in count:

            while start <= end < s_len:
                t = s[start]
                if t in count:
                    count[t] += 1
                start += 1
            end = start
            # count = Counter(p)
            k = n
            continue

        else:

            if count[ch] > 0:
                count[ch] -= 1
                k -= 1

            elif count[ch] == 0:

                while start < s_len and s[start] != ch:
                    t = s[start]
                    count[t] += 1
                    start += 1
                k = n - (end - start)
                start = start + 1

        if k == 0:
            output.append(start)
            k = 1
            count[s[start]] += 1
            start += 1

        end = end + 1
    return output


s = 'abba'
p = 'ab' # [0, 2]

#
s = 'abcab'
p = 'abc' # [0, 1, 2]


# s = 'ba'
# p = 'ab' # [0]


#
# s = 'bba'
# p = 'ab' # [1]


# s = 'abba'
# p = 'abb' # [0, 1]


#
# s = 'abcabc'
# p = 'abc' # [0, 1, 2, 3]


# s = 'abab'
# p = 'ab' # [0, 1, 2]



# s = 'cbaebabacd'
# p = 'abc' # [0, 6]



# s = 'abdbebc'
# p = 'bbadec' # no output


# s = 'abdbebca'
# p = 'bbadec' # [2]


s = 'zabczacb'
p = 'bc' # [2, 6]


#
# s = "abacbabc"
# p = "abc" # [1, 2, 3, 5]


print(findAnagrams(s, p))






