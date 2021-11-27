# Construct the longest palindrome by shuffling or deleting
# characters from a given string
def longestPalindrome(str):
    # create a dictionary for characters of a given string
    freq = {}

    for ch in str:
        freq[ch] = freq.get(ch, 0) + 1

    left = ""  # stores left substring

    # iterate through the frequency dictionary
    for ch, count in freq.items():

        # if the current character's frequency is odd,
        # update mid to current (and discard the old one)
        if count % 2 == 1:
            mid = ch  # stores odd

        # append half of the characters to the left substring
        # (the other half goes to the right substring in reverse order)
        for i in range(count // 2):
            left += ch

    # the right substring will be the reverse of the left substring
    right = left[::-1]

    # return formed by the left substring, mid-character (if any),
    # and the right substring
    return left + mid + right

s = 'abbaccd'
s = 'abbaccddd'
print(longestPalindrome(s))
