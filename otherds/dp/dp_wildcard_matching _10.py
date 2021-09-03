from typing import List


def util(text, pattern, cache):

    if (text, pattern) in cache:
        # print('cache hit')
        return cache[(text, pattern)]

    if not text and not pattern:
        cache[(text, pattern)] = True
        return True

    if not pattern:
        cache[(text, pattern)] = False
        return False

    # print('matching: {}, {}'.format(text, pattern))

    if len(pattern) == 1 and pattern[0] == '*':
        cache[(text, pattern)] = True
        return True

    if len(text) <= 1 and pattern[-1] == '*':
        return util(text, pattern[:-1], cache)

    if not text:
        cache[(text, pattern)] = False
        return False

    last_pattern = pattern[-1]

    if last_pattern == '*':
        n = len(text)
        v = False
        for i in range(1, n):
            v = util(text[:-i], pattern[:-1], cache)
            if v:
                cache[(text, pattern)] = True
                return True
        # v = util(text[:-1], pattern, cache)
        r = util(text, pattern[:-1], cache)
        cache[(text, pattern)] = r or v
        return r or False
    elif last_pattern == '?' or last_pattern == text[-1]:
        return util(text[:-1], pattern[:-1], cache)
    else:
        cache[(text, pattern)] = False
        return False


def isMatch(s: str, p: str) -> bool:
    """

     if '*' is present, it would be at pattern[1].p

          case 1: either entire text matches remaining pattern
          case 2: ignoring this text character at this position, remaining text matches the remaining pattern
    else:
        if pattern[0] is one of { '.', or text[0] }, recur for remaining text and pattern
    """
    cache = {}
    return util(s, p, cache)

s = 'abc'
p = 'a*c'

s = 'bacb'
p = '*?*'

s = 'abcdef'
p = '*'

s = 'abc'
p = 'b*'

s = 'abc'
p = '******'

# s = 'cb'
# p = '?a'
#
#
# s = 'adceb'
# p = '*a*b'
#
# s = 'acdcb'
# p = 'a*c?b'

s = "mississippi"
p = "m??*ss*?i*pi"

# s = "abcabczzzde"
# p = "*abc???de*"   # True

s = "bbbababbabbbbabbbbaabaaabbbbabbbababbbbababaabbbab"
p  = "a******b*"

s = "aabbbbaaaaaaaabbbabbaabbbbbbaabaaabbbabbaabaaabababbaabababbaaaaababbbbbbababaaabbbbbabbbaabaaaaaaabbbbbbababbaaaabbababbbbabbabbabababbaabbbabbabbaabababbaaabbaabaabbbbaabaaaabbbbbbabaabaabbabaaabbbbab"
p = "a**abaaa******a*b*ba**aba***b*bbbab*bb*aab**a*bba*b*abab**aabbb***a*a**b**a*abab*ba**aa**b***aba*b****a*"

# s = "bbbbaaaaabaabbbbaabaaabaabbababbbaaabbababbbabaabaabaabababaaabaaaabbaabbaabbaaaaabbabbbbaaaababbaaaabbabbbaabaaabbaabaabaaababbabbaababaababbbbbaabbabbabbbbaabbaaababbabaaabbbbbbbbaababbbbbbabbaabaaa"
# p = "b*a**b***abaabaaaba*abaaaaabaabb*bbb*aa*ab*a**b**b*a**a**a*abbb***bb*b*****baababaa**ab*aa*bbaba**bb*b*"  # FALSE

print(isMatch(s, p))

