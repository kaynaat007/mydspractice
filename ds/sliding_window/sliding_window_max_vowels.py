

def vowels_in_substring(s, k):
    """
    return max number of vowel letters in any substring of s with length k.
    """
    vowels_dict = { 'a', 'e', 'i', 'o', 'u'}
    n = len(s)
    slow = 0
    fast = 0
    max_vowel = 0
    vowels = 0
    if n == 0:
        return 0
    while slow < n and fast < n:

        if fast - slow + 1 > k:

            slow = slow + 1

        if s[fast] in vowels_dict:
            vowels = vowels + 1

        if slow - 1 >= 0 and s[slow-1] in vowels_dict:
            vowels = vowels - 1
            slow = slow + 1

        max_vowel = max(max_vowel, vowels)
        fast = fast + 1
    return max_vowel


s = 'abcae'
k = 3

s = 'abciiidef'
k = 3

s = 'aeiou'
k = 2

s = 'leetcode'
k = 3

s = 'rhythms'
k = 4

s = 'tryhard'
k = 4

print(vowels_in_substring(s, k))